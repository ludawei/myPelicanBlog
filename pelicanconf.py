#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'admin'
SITENAME = u"分享是美德"

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [('首页', '/'), ('归档', '/archives'), ('分类', '/categories'), ('标签', '/tags'), ('关于我', '/aboutme')]

SUMMARY_MAX_LENGTH = 10

PATH = 'content'

TIMEZONE = 'Europe/Paris'
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'jp': '%Y-%m-%d(%a)',
    'zh': '%Y年%m月%d',
}

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/ludawei'),
          ('cnblog', 'http://www.cnblogs.com/china-ldw/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# 主题
THEME = "/Users/ludawei/pelican-themes/gum"


# 插件路径
PLUGIN_PATHS = ['/Users/ludawei/pelican-plugins']
# 添加插件
PLUGINS = ['tag_cloud',]

# tag_cloud 配置(自己个性配置)
DISPLAY_TAGS_INLINE = True
DISPLAY_TAGS_ON_SIDEBAR = True
TAG_CLOUD_STEPS = 4

GOOGLE_ANALYTICS_ID = 'UA-77750244-1'
DISQUS_SITENAME = u"davlu"
