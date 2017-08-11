Title: mysql时间转换
Date: 2017-02-22
Tags: mysql
Category: mysql
Slug: mysql_time_format

mysql常用的时间转换方法
```php
1，字符串转Date
str_to_date(str, format)

select str_to_date('08/09/2008 08:09:30', '%m/%d/%Y %h:%i:%s');             -- 2008-08-09 08:09:30

2，Date转字符串
date_format(date, format)

select date_format('2008-08-08 22:23:01', '%Y%m%d%H%i%s');                  -- 20080808222301

3，Date转时间戳
UNIX_TIMESTAMP(date)   // 参数需要是Date类型

Select UNIX_TIMESTAMP('2006-11-04 12:23:00');                               -- 1162614180

4，时间戳转Date
FROM_UNIXTIME(timestamp)
select FROM_UNIXTIME(1156219870);                                           -- 2006-08-22 12:11:10

由以上可以衍生出，
5，字符串转时间戳
UNIX_TIMESTAMP(str_to_date(time_str, format))   

select UNIX_TIMESTAMP(str_to_date('2017022210', "%Y%m%d%H"));               -- 1487728800
ps:在where条件选择时非常好用

6，字符串格式化
DATE_FORMAT(str_to_date(time_str, from_format), to_format)

select DATE_FORMAT(str_to_date("2017022210", "%Y%m%d%H"), "%Y%m%d");        -- 20170222
ps:在输出到结果中时，格式化时间非常必要
```
