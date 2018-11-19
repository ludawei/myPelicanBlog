Title: bash使用学习
Date: 2018-10-23
Tags: linux, bash
Category: bash
Slug: linux-bash-use-tips


```bash
#变量赋值注意
currDir = 'hello'      #错误，=左右不能有空格
currDir='hello'        #正确

#得到执行结果
currDir=`dirname $0`        #方法1
currDir=$(dirname $0)       #方法2

#时间
curD=`date +"%Y%m%d"`
echo $curD

#if条件控制
a=`ps -ef | grep "python" | grep -v grep | awk {'print $2'} | head -1`      #head -1：只取1行
if [ -z $a ]            #判断是否为空
then
    echo "为空"
else
    echo "不为空"
fi

#for循环
for i in '111 222 333'
do
    echo ${i}
done

#文件读取
file_c=`cat /Users/ludawei/test_ftp.txt`
echo $file_c

#一个监控进程的例子
for i in 'python' 'ffmpeg' 'php'
do
    a=`ps -ef | grep $i | grep -v grep | awk {'print $2'} | head -1`      #head -1：只取1行
    if [ -z $a ]            #判断是否为空
    then
        echo "$i进程为空"
    else
        echo "$i进程不为空"
    fi
done
```