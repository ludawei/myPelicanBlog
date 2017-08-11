Title: Xcode修改项目名字
Date: 2017-04-20
Tags: Xcode
Category: iOS
Slug: xcode-change-program-name
Summary: Xcode修改项目名字，其实也没那么麻烦~

1，xcode版本  
￼![img](../images/xcode_version.png)


2，修改工程文件名，直接修改（提示->确定）  
￼![img](../images/760036C4-4EB1-4466-A65F-04B213C3C0CC.png)￼

选中工程文件，在右侧的属性栏里修改工程名，如下图  
￼￼![img](../images/760036C4-4EB1-4466-A65F-04B213C3C0CC.png)


3，修改工程目录名（分两步）  
a）修改目录名  
![img](../images/110462FB-B2FF-403C-B08E-2C62440394BC.png)

b）修改目录指向  
￼![img](../images/2AE4082E-B519-4455-9B33-32A0E7C511A5.png)


4，如果info.plist路径报错，需要重新选择info.plist  
General->Identity，重新选择info.plist文件  

5，修改PrefixHeader.pch路径  
target->Build Settings->Prefix Header，修改为新的路径  

6，如果有推送，还需要重新生成证书  
Capabilities->Push Notifications，关闭后重新打开一次就好了，删除原来多余的  

Done！Enjoy it~
