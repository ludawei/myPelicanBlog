Title: 几种常用语言下的sha1加密
Date: 2017-04-10
Tags: sha1, hmac
Category: iOS
Slug: sha1-encode-in-some-code-language
Summary: 几种常用语言下的sha1加密

为了防止api数据被第三方（非己方）的网页或App调用到，我们需要对一些关键数据接口做api请求的身份验证；
我们这用到的方法是，提供一个分配好的appid（应用id）和private_key（私钥），然后按一个特定规则计算出一个key参数传给服务器。


python实现
```python
#encoding:utf8
import os, json, datetime, hmac, base64
from hashlib import sha1
from urllib import quote_plus
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# private_key and appid
private_key = 'my_test'
appid = '1234567890'

date = datetime.datetime.now().strftime("%Y%m%d%H%M")
domain = "http://xxxxxx.com/?lon=118.246&lat=39.117&type=test"

# get public_key
public_key = domain + "&date=" + date + "&appid=" + appid
print public_key
# 哈希一个令牌
key = base64.b64encode(hmac.new(private_key, public_key, sha1).digest())

url = domain + "&date=" + date + "&appid=" + appid + "&key=" + quote_plus(
    key)
print url

# 结果如下：
# http://xxxxxx.com/?lon=118.246&lat=39.117&type=test&date=201704131538&appid=1234567890&key=Mw8m6gidwkLZaQRwzb6uIoFVc4Y%3D

```

php实现
```php
<?php
// private_key
$private_key = 'my_test';
$appid = '1234567890';

$date=date("YmdHi");
$domain = "http://xxxxxx.com/?lon=118.246&lat=39.117&type=test";

// get public_key
$public_key = $domain."&date=".$date."&appid=".$appid;

# get key
$key = base64_encode(hash_hmac('sha1',$public_key,$private_key,TRUE));

$URL = $domain."&date=".$date."&appid=".$appid."&key=".urlencode($key);
echo $URL."<br />";
?>


// 结果如下：
// http://xxxxxx.com/?lon=118.246&lat=39.117&type=test&date=201704130739&appid=1234567890&key=kU7DVthCC0wjWTrI5Jtri2nA%2BMY%3D

```

js实现：
```js

var crypto = require('crypto')

private_key = 'my_test'
appid = '1234567890'

var time = new Date()
var y = time.getFullYear()
var m = time.getMonth()+1
var d = time.getDate()
var h = time.getHours()
var mm = time.getMinutes()
var s = time.getSeconds()
date = y+''+m+''+d+''+h+''+mm

domain = "http://xxxxxx.com/?lon=118.246&lat=39.117&type=test"
public_key = domain + "&date=" + date + "&appid=" + appid

var hmac = crypto.createHmac('sha1', private_key)
hmac.write(public_key)
hmac.end()
var key = hmac.read().toString('base64')
key = encodeURIComponent(key)

finalUrl = domain +'?appid='+ appid +'&timestamp='+ date +'&key='+ key
console.log(finalUrl)

// 结果如下：
// http://xxxxxx.com/?lon=118.246&lat=39.117&type=test?appid=1234567890×tamp=20174131551&key=JPBPvqvtjQbgelt70crbOJN3v9o%3D

```

Objective-C实现
```objc

NSString *private_key = @"my_test";
NSString *appId = @"1234567890";
NSString *domain = @"http://xxxxxx.com/?lon=118.246&lat=39.117&type=test";

NSDateFormatter *formatter = [NSDateFormatter new];
[formatter setDateFormat:@"yyyyMMddHHmm"];
NSString *now = [formatter stringFromDate:[NSDate date]];

NSString *public_key = [NSString stringWithFormat:@"%@&date=%@&appid=%@", domain, now, appId];

const char *cKey  = [private_key cStringUsingEncoding:NSASCIIStringEncoding];
const char *cData = [public_key cStringUsingEncoding:NSASCIIStringEncoding];

//sha1
unsigned char cHMAC[CC_SHA1_DIGEST_LENGTH];
CCHmac(kCCHmacAlgSHA1, cKey, strlen(cKey), cData, strlen(cData), cHMAC);

NSData *HMAC = [[NSData alloc] initWithBytes:cHMAC length:sizeof(cHMAC)];

NSString *key = [HMAC base64EncodedStringWithOptions:0];
key = (NSString *)CFBridgingRelease(CFURLCreateStringByAddingPercentEscapes(
                                                                      NULL,
                                                                      (__bridge CFStringRef)key,
                                                                      NULL,
                                                                      (CFStringRef)@"!*'\"();:@&=+$,/?%#[]% ",
                                                                      CFStringConvertNSStringEncodingToEncoding(NSUTF8StringEncoding)));
NSString *url = [NSString stringWithFormat:@"%@&date=%@&appid=%@&key=%@", domain, now, appId, key];
NSLog(@"%@", url);

// 结果如下：
// http://xxxxxx.com/?lon=118.246&lat=39.117&type=test&date=201704131613&appid=1234567890&key=%2BteLBODxDGS13d9BuVJQMNZbbzs%3D
```
