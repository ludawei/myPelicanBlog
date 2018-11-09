Title: nginx 部分使用技巧
Date: 2018-09-17
Tags: linux, nginx
Category: nginx
Slug: linux-nginx-tips

#### **centos6.4安装nginx问题**
1，安装时提示 No more mirrors to try。
```bash
#解决：配置yum源。（https://blog.csdn.net/u012141686/article/details/79549999）
wget http://dl.Fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
rpm -ivh epel-release-latest-7.noarch.rpm
```

2，正常安装、配置完后台，无法访问。（防火墙问题）
```bash
#解决：配置防火墙。（参考：https://www.cnblogs.com/liscookie/p/4032782.html）
vi /etc/sysconfig/iptables                                              #配置防火墙
-A INPUT -m state --state NEW -m tcp -p tcp --dport 80 -j ACCEPT        #开启80端口
service iptables restart                                                #重启防火墙
```

#### **nginx命令**
```bash
#查找nginx服务是否启动
ps -ef | grep nginx
#检测配置文件
nginx -t
#重启
nginx -s reload
```

#### **web文件服务器**
```nginx
location /data/test/
{
        alias   /data/home/dav/test/;
        add_header Access-Control-Allow-Origin *;
        autoindex on;
        charset utf-8;
        #autoindex_format json;            #是否以json格式显示
        autoindex_exact_size off;
        autoindex_localtime on;
}
```

#### **端口转发**
```nginx
location /alert/my_baidu 
{
        add_header Access-Control-Allow-Origin *;           #解决跨域问题
        proxy_pass http://www.baidu.com;
        proxy_set_header Host $host;
}

#nginx加载PHP配置
location ~ \.php$ {
        #include snippets/fastcgi-php.conf;
        try_files $uri $uri/ =404;
        fastcgi_split_path_info ^(.+\.php)(/.+)$;
        fastcgi_pass unix:/run/php/php7.0-fpm.sock;
        fastcgi_index index.php;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
}
#nginx加载flask配置(flask运行在5001端口)
location /test_flask/
{
        proxy_pass http://127.0.0.1:5001/;
        add_header Access-Control-Allow-Origin *;       
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header REMOTE-HOST $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_read_timeout 20s;
}
```
