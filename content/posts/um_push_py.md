Title: python友盟推送
Date: 2017-02-17
Tags: python
Category: python
Slug: um_push_py

python实现友盟推送
```python
# iOS
import requests, time
import json, hashlib

data = {
    "appkey": "友盟申请的appKey",
    "production_mode": "true",
    "type": "groupcast",
    "payload": {
        "aps": {
            "sound": "自定义.caf",
            "alert": {
                "body": "这是一条推送的消息",
                "title": "推送消息",
            }
        },
        "myKey1": "value" # 自定义参数
    },
    "filter": { # 过滤条件
        "where": {
            "and": [{
                "and": [{
                    "tag": "tag1"
                }, {
                    "tag": "tag2"
                }]
            }]
        }
    }
}

data['timestamp'] = str(int(time.time()))
postBody = json.dumps(data)
sign_md5 = hashlib.md5()
sign_md5.update("POST" + um_url + postBody + appSecret)
sign = sign_md5.hexdigest()
url = um_url + "?sign=" + sign
r = requests.post(url, data=postBody)
print r.text

#Android
data = {
    "appkey": "友盟申请的appKey",
    "production_mode": "true",
    "type": "groupcast",
    "payload": {
        "extra": {
            "myKey1": "value" # 自定义参数
        },
        "display_type": "notification",
        "body": {
            "title": "app名称",
            "ticker": "app名称",
            "text": "这是一条推送的消息",
            "custom": "1",
            "after_open": "go_custom",
            "play_vibrate": "true",
            "play_sound": "true",
            "play_lights": "true"
        }
    },
    "filter": {
        "where": {
            "and": [{
                "and": [{
                    "tag": "tag1"
                }, {
                    "tag": "tag2"
                }]
            }]
        }
    }
}

data['timestamp'] = str(int(time.time()))
postBody = json.dumps(data)
sign_md5 = hashlib.md5()
sign_md5.update("POST" + um_url + postBody + appSecret)
sign = sign_md5.hexdigest()
url = um_url + "?sign=" + sign
r = requests.post(url, data=postBody)
print r.text
```

参考：<http://dev.umeng.com/push/ios/%E6%9C%8D%E5%8A%A1%E7%AB%AF%E4%BB%A3%E7%A0%81%E8%B0%83%E7%94%A8%E7%A4%BA%E4%BE%8B>
