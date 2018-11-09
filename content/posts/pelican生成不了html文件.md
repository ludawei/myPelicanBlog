Title: pelican 生成不了html文件
Date: 2018-04-03
Tags: pelican, markdown
Category: pelican
Slug: pelican-can-not-create-html

今天用peclican转md文件生成html时，终端提示`WARNING: No valid files found in content.`

更新peclican也没用，最后发现是markdown库安装不对
```bash
#错误的安装
pip install Markdown
#正确的安装 
easy_install -U markdown

```
感谢[文章](https://www.linuxzen.com/jiang-pelicanban-ben-geng-xin-dao-33.html)，解决了问题