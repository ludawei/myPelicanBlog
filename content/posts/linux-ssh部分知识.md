Title: linux ssh部分知识
Date: 2018-08-15
Tags: linux, ssh
Category: linux
Slug: linux-ssh-tips

#### **ssh别名**
别名配置文件：~/.ssh/config
```
Host dav1
HostName xx.xx.xx.11
User dav
Port 22
IdentityFile ~/.ssh/id_rsa

Host dav2
HostName xx.xx.xx.22
User dav
Port 22
IdentityFile ~/.ssh/id_rsa
```
配置完后，可以使用别名连接服务器（不用输入ip），如下：
```bash
# 相当于 ssh -p 22 dav@xx.xx.xx.11
ssh dav1 
# 相当于 ssh -p 22 test@xx.xx.xx.11
ssh test@dav1 
```

#### **sss免密**
```bash
#方法1：一行命令（有时会莫名其妙失败）
ssh-copy-id -i .ssh/id_rsa.pub dav@xx.xx.xx.11
#方法2：
#复制本机A公钥到目标服务器B
scp -P 2222 .ssh/id_rsa.pub dav@xx.xx.xx.11:/home/dav/
#修改服务器B文件权限（权限不能多也不能少，ssh通过权限判断安全性）
chmod 600 ~/.ssh/authorized_keys
#将A机器公钥写入
cat id_rsa.pub  >> .ssh/authorized_keys
```

#### **ssh隧道（反向代码，穿透内网）**
准备条件：  
1，两台机器：公网机器A（ip：xx.xx.xx.11），内网机器B（ip：xx.xx.xx.22）  
2，公网机器A开放54637端口  
3，内网机器B做对A的免密ssh  
4，在内网机器B执行ssh反向代理命令  
```bash
#内网
#ssh方法
ssh -f -N -o "ServerAliveInterval 60" -o "ServerAliveCountMax 3" -R 0.0.0.0:54637:127.0.0.1:22 -p 22 dav@xx.xx.xx.11
#autossh方法（需要安装autossh，断了可以自动重新启动）
autossh -fN -o "PubkeyAuthentication=yes" -o "StrictHostKeyChecking=false" -o "PasswordAuthentication=no" -o "ServerAliveInterval 60" -o "ServerAliveCountMax 3" -R 0.0.0.0:54637:127.0.0.1:22 -p 22 dav@xx.xx.xx.11

#释义：将本机（内网机器A）的22端号代理到公网机器A的54637端口

#在外网环境下，机器C上连接内网机器A命令（相当于：ssh -p 22 dav@xx.xx.xx.22 ）
ssh -p 54637 dav@xx.xx.xx.11 
```

#### **sshpass**
`sshpass`了解一下...