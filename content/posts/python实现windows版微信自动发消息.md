Title: python实现windows版微信自动发消息（模拟键盘鼠标）
Date: 2018-12-28
Tags: windows, python
Category: python
Slug: python-windows-wecat-sender

18年12月，微信发布7.0后，原来用wxpy库（基于网页版）做的自动发信息脚本出问题了--网页微信的登录状态只能保存10分钟了（原来可以一直保存），这样定时发消息的功能算是报费了，只能另寻出路。

近日找到模拟键盘鼠标+复制粘贴的的方法试了下，可以初步完成目前的使用需要，代码如下：
```python
# -*- coding=utf-8 -*-
import json,os,sys,glob
from pynput.mouse import Controller as Mouse
from pynput.mouse import Button as bt
from pynput.keyboard import Controller as Keyboard
from pynput.keyboard import Key 
import time
import win32clipboard as w
import win32con
import win32api
import requests
from threading import Timer
import datetime

reload(sys)
sys.setdefaultencoding('utf-8')

def get_new():
    text = "我是一条测试消息"

    return text

def setClipboardText(aString):  # 写入剪切板  
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardText(aString, win32con.CF_UNICODETEXT)
    w.CloseClipboard()

def getClipboardText():  # 读取剪切板  
    w.OpenClipboard()
    d = w.GetClipboardText(win32con.CF_UNICODETEXT)
    w.CloseClipboard()
    return d

def sendWX():
    ms=Mouse()
    kb=Keyboard()
    # print(ms.position)
    # time.sleep(3)
    # print('The current pointer position is {0}'.format(ms.position))

    # 得到消息内容
    text = get_new()
    # print text

    # 消息内容写入系统剪切板
    setClipboardText(text)
    # print getClipboardText()
    #set pointer positon

    # 切换微信窗口焦点
    ms.position = (893, 449)
    print('The current pointer position is {0}'.format(ms.position))
    ms.press(bt.left)
    ms.release(bt.left)

    # 粘贴消息内容
    kb.press(Key.ctrl)
    kb.press('v')
    kb.release('v')
    kb.release(Key.ctrl)

    # 点击enter, 发送消息
    kb.press(Key.enter)
    kb.release(Key.enter)

if __name__ == "__main__":
    sendWX()
```

然后将python脚本写入到windows计划任务，定时1小时执行一次。

PS：  
脚本还是有些缺陷，实际使用时，把脚本放到windows云服务器上运行，结果发现在没有远程桌面时（即无GUI时），脚本无法模拟键盘鼠标而执行失败，只能一直开着远程才能执行成功~~~

目前正在寻找更完美的实现办法...

参考资源：  
https://www.jianshu.com/p/03010ac70e4c  
https://www.jianshu.com/p/a9c28cb24c05  
http://www.voidcn.com/article/p-yekwwmnm-bbb.html  