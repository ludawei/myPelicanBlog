Title: linux 部分常用命令
Date: 2018-08-16
Tags: linux, bash
Category: bash
Slug: linux-bash-tips

#### **rsync同步命令**
```bash
#参数说明：
#-a 参数，相当于-rlptgoD（-r 是递归 -l 是链接文件，意思是拷贝链接文件；-p 表示保持文件原有权限；-t 保持文件原有时间；-g 保持文件原有用户组；-o 保持文件原有属主；-D 相当于块设备文件）；
#-z 传输时压缩；
#-P 传输进度；
#-v 传输时的进度等信息；
#--delete 删除同步目标目录的多余文件（与同步源一致）
rsync -avzP --delete root@{remoteHost}:{remoteDir}/* {localDir}

#远程文件复制（基于ssh）
scp 11.txt dav@xx.xx.xx.xx:/data/home/dav/test              #复制本地文件到远程
scp -r ~/test dav@xx.xx.xx.xx:/data/home/dav/test/          #复制本地目录到远程
scp dav@xx.xx.xx.xx:/data/home/dav/test/11.txt ~/test       #复制远程文件到本地
scp -r dav@xx.xx.xx.xx:/data/home/dav/test ~/test/          #复制远程目录到本地

#查找进程
ps -ef|grep 'test shell'|grep -v 'grep'     #配合crontab可以做进程监控
#查找并终止进程
ps -ef|grep 'test shell'|grep -v 'grep'|awk '{print $2}'|xargs --no-run-if-empty kill -9

#查看目录中所有目录、文件大小： 
du -hs *
#(带排序)
du -hs * | sort -h

#修改用户所在组
id                              #查看所属组
usermod -a -G sudo dav          #添加sudo权限（-a追加）
usermod -G dav dav              #取消sudo权限（去掉-a表示指定用户组）

#修改用户信息
usermod -s /bin/bash dav        #允许用户登录
usermod -s /bin/false dav       #禁止用户登录
usermod -s /sbin/nologin dav    #禁止用户登录
#root专用
passwd                          #修改root的密码，直接用passwd
passwd dav                      #修改普通用户的密码，passwd后加用户名

#设置crontab默认编辑器为vim
export EDITOR=vim

# 删除历史数据 3天前
find /home/dav/test/ -type f -mtime +2 -delete
find /home/dav/test/ -type f -mtime +2 -size +10c -delete       #大于10bytes
# 删除空目录
find /home/dav/test/ -type d -empty -delete
# 查找并复制
find http_files/ -name '*).mp4' -exec cp {} /home/dav/tmp_files/ \;
# 查找并mv
find /home/dav/http_files -type f -exec mv {} $(date -d "today" +"%Y%m%d")/ \;

#查找文件包含内容
find . -name '*' | xargs grep 'test'

#创建软链接
ln -s /home/dav/test test       #在当前创建指向/home/dav/test的软链接
#删除软链接
unlink test

#sshfs
sshfs dav@10.141.2.196:/data/home/dav/test /data/home/dav/test  #Linux 挂载远程目录（将dav@10.141.2.196机器上的目录挂载到本地，要做ssh免密）
umount /data/home/dav/test                                      #删除挂载

#硬盘挂载
mount -t nfs xx.xx.xx.xx:/mount/test /backup
#重新挂载
umount
mount -a

#linux压缩
tar -zcvf /home/dav/xxx.tar.gz /xxx
#解压
tar -zxvf xxx.tar.gz
```
