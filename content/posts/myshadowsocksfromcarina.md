Title: 在carina上使用Docker搭建免费的ShadowSocks
Date: 2016-06-02
Tags: carina, ShadowSocks, Docker, textnow
Category: 科学上网
Slug: 在carina上使用Docker搭建免费的ShadowSocks
Summary: 科学上网之 - 在carina上使用Docker搭建免费的ShadowSocks

Carina是Rackspace旗下的一个网站，提供了Docker服务。最近，看到消息可以在该网站上注册账号，免费试用Docker服务。竟然有这么好的事，于是尝试注册了一个账号，搭建了一个免费的shadowsocks服务器。

**账号注册**

textnow提供无限的美国和加拿大短信收发，并且提供有免费的一个美国电话号码.不同于heywire的是这个虚拟号在国内完全可以访问，而且收发的速度都是一流，在手机端登陆也是很快就可以收发到短信

<http://www.textnow.com/>

账号：facebook账号(本人的)<br />
号码：(917) 636-7274（本人的）

**安装Boot2Docker**

Boot2Docker是帮助控制虚拟机中Docker的工具，它会下载一个安装好docker的虚拟机，并控制其实现docker功能。

在mac下安装boot2docker只要执行

```
brew install boot2docker
```

即可。

**配置Docker CLI**

点击cluster下面的按钮Get access，下载一个Docker集群配置信息文件。

解压后，进入该目录。source docker.env设置合适的docker环境变量：

```
source docker.env
```

查看是否连接上：

```
➜ docker info
Containers: 11
Images: 6
Role: primary
Strategy: spread
Filters: health, port, dependency, affinity, constraint
Nodes: 1
2ede2591-1ec0-4c2b-a3ef-59697ff02ba7-n1: 104.130.22.24:42376
  └ Status: Healthy
  └ Containers: 11
  └ Reserved CPUs: 0 / 12
  └ Reserved Memory: 0 B / 4.2 GiB
  └ Labels: com.docker.network.driver.overlay.bind_interface=eth1, executiondriver=native-0.2, kernelversion=3.18.21-2-rackos, operatingsystem=Debian GNU/Linux 7 (wheezy) (containerized), storagedriver=aufs
  └ Error: (none)
  └ UpdatedAt: 2016-04-15T11:53:04Z
Kernel Version: 3.18.21-2-rackos
Operating System: linux
CPUs: 12
Total Memory: 4.2 GiB
Name: 2ede2591-1ec0-4c2b-a3ef-59697ff02ba7-n1
```




可以看到cluster中结点的具体信息。

通过Docker安装shadowsocks

通过Docker安装shadowsocks非常方便，只需要一个命令：

```
docker run -d --name shadowsocks -p 8989:8989 oddrationale/docker-shadowsocks -s 0.0.0.0 -p 8989 -k xxxxxx -m aes-256-cfb
```

-p是设置shadowsocks的服务器端口号；-k后面设置自己的密码。

使用docker ps查看是否安装成功：

```
➜  docker ps

CONTAINER ID        IMAGE                             COMMAND                  CREATED             STATUS              PORTS                         NAMES
3d21228c5ce1        oddrationale/docker-shadowsocks   "/usr/local/bin/ssser"   8 seconds ago       Up 7 seconds        172.99.70.21:8989->8989/tcp   73eb155d-807d-4453-af3a-45068088827b-n1/shadowsocks
0dd57ba46081        carina/consul                     "/entrypoint.sh agent"   31 minutes ago      Up 31 minutes                                     73eb155d-807d-4453-af3a-45068088827b-n1/carina-svcd
```

可以看到shadowsocks服务已经在运行了。

使用port命令，可以查看shadowsocks服务的IP和端口：

```
➜  docker port shadowsocks
8989/tcp -> 172.99.70.21:8989
```

记住shadowsocks的IP和端口号，待会儿需要填入shadowsocks代理软件中。

完成！

参考：<br />
1，[免费短信收发](http://zzsa.net/%E5%9B%BD%E5%86%85%E5%A4%96%E4%B8%80%E4%BA%9B%E5%85%8D%E8%B4%B9%E7%BD%91%E7%BB%9C%E8%99%9A%E6%8B%9F%E7%94%B5%E8%AF%9D-%E5%85%8D%E8%B4%B9%E7%9F%AD%E4%BF%A1%E6%94%B6%E5%8F%91-%E5%85%8D%E8%B4%B9%E4%BC%A0/)<br />
2，[在carina上使用Docker搭建免费的ShadowSocks](http://www.wengweitao.com/zai-carinashang-shi-yong-dockerda-jian-mian-fei-de-shadowsocks.html)<br />
3，[不花一分钱，搭建一个完全免费的Shadowsocks服务器](http://www.rendoumi.com/wan-quan-mian-fei-de-shadowsocksfu-wu-qi/)<br />
4，[在Mac下安装使用Docker](http://yansu.org/2014/04/10/install-docker-in-mac.html)<br />
5，[深入浅出Docker（二）：Docker命令行探秘](http://www.infoq.com/cn/articles/docker-command-line-quest)
