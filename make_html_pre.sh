#/bin/bash

currDir=`dirname $0`
cd $currDir

# echo $currDir
make html
open http://localhost:8000/

echo "开启服务，本地预览：http://localhost:8000/"

make serve