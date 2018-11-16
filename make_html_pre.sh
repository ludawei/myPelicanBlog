#/bin/bash

currDir=`dirname $0`
cd $currDir

# echo $currDir
make html
open http://localhost:8000/

echo "同步文件到139.199.23.228"
sshpass -p 'LvGWLru4RwtNGSzw2zQl' rsync -avz --exclude "*.git" --exclude "*.DS_Store" /Users/ludawei/important/ludawei_blog_github/* dav@139.199.23.228:/home/dav/www/blog/

echo "开启服务，本地预览：http://localhost:8000/"

make serve