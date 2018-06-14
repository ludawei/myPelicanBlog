Title: Universal Link支持上手
Date: 2018-02-09
Tags: iOS
Category: iOS
Slug: iOS-Universal-Link

Universal Links是iOS9推出的一项功能，使你的应用可以通过传统的HTTP链接来启动APP(如果iOS设备上已经安装了你的app，不管在微信里还是在哪里)， 或者打开网页(iOS设备上没有安装你的app)。

操作步骤：

1，准备https服务器；

2，开发者中心证书打开Associated Domains（通常一个App会有正式版、测试版、企业版，多个都可以配置上）；

3，工程配置Associated Domains（applinks可以添加多个服务器）；

4，appDelegate代码添加：
```
- (BOOL)application:(UIApplication *)application continueUserActivity:(NSUserActivity *)userActivity restorationHandler:(void (^)(NSArray * _Nullable))restorationHandler{
    return YES;
}

- (BOOL)application:(UIApplication *)application openURL:(NSURL *)url sourceApplication:(NSString *)sourceApplication annotation:(id)annotation
{
    return YES;
}
```
5，创建apple-app-site-association的json文件，不带.json后缀；

6，将apple-app-site-association文件放在服务器域名对应目录的.well-know目录下（可以放置于多台服务器）,并将文件返回的content_type设置为application/json；

7，安装配置完成的App，打开相应域名下apple-app-site-association文件中符合paths规则的任一网页测试；


PS：测试网页与内容无关，空白页面也可以测试；测试要注意顺序，配置好apple-app-site-association后，重新安装App，再打开或者刷新网页测试效果


以下是我配置的apple-app-site-association文件
```json
{
    "applinks": {
        "apps": [],
        "details": [
            {
                "appID": "temaId.boundId1",
                "paths": [ "/Public/share/chinaweather_links/", "/Public/share/chinaweather_links/*", "/jueceqixiang.html" ]
            },
            {
                "appID": "temaId.boundId2",
                "paths": [ "/Public/share/chinaweather_links/", "/Public/share/chinaweather_links/*", "/jueceqixiang.html" ]
            }
        ]
    }
}
```
apple-app-site-association内容说明：

1，apps空着不用动

2，paths在不同服务器上的目录路径不同

参考：
[https://developer.apple.com/library/content/documentation/General/Conceptual/AppSearch/UniversalLinks.html#//apple_ref/doc/uid/TP40016308-CH12-SW1]

[http://awhisper.github.io/2017/09/02/universallink/]
