Title: ffmpeg使用命令记录
Date: 2018-05-08
Tags: ffmpeg
Category: ffmpeg
Slug: ffmpeg-use

一些工作中常用到的ffmpeg命令：
```bash

#图片合成视频
ffmpeg -framerate 25 -pattern_type glob -i 'images/*.png' -c:v libx264 -pix_fmt yuv420p out2.mp4
#视频转码
ffmpeg -i ~/Desktop/out.mpg -vcodec libx264  -crf 20 ~/Desktop/out.mp4
#屏幕录制（mac）
ffmpeg -f avfoundation -i "1:0" -ss 00:00:05 -t 00:00:05 -pixel_format monob ~/Desktop/out.mpg
#屏幕录制（windows,指定窗体）
ffmpeg -f gdigrab -draw_mouse 0 -framerate 25 -i title="decision weather - Google Chrome" out.mpg
#屏幕录制（windows,指定屏幕区域）
ffmpeg -f gdigrab -framerate 30 -offset_x 0 -offset_y 0 -video_size 1600x900 -i desktop out.mpg
- gdigrab:表明我们是通过gdi抓屏的方式； 
-framerate 30：表示我录制的帧率为30；
-offset_x ：左上偏移量X； 
-offset_y ：左上偏移量Y； 
-video_size：需要录制的宽度和高度，这是我是整个屏幕； 
-i：输入路径和名称以及格式mpg； 
-desktop：告诉ffmpeg我们录的是屏幕，而不是一个窗口(可以录制一个窗口，不过得用窗口的ID)。
说明：帧率是和格式相关的，比如我用mpg格式30帧就很清楚，如果用mp4则需要60帧。

#视频剪辑
ffmpeg -i test.mp4 -ss 2:59:00 -codec copy -t 60 output.mp4 （取最后60秒视频）
#修改视频码率
ffmpeg -i test.mp4 -vb 20M -max_muxing_queue_size 20480 -y output.mp4

#rtmp推流
ffmpeg -re -i test.mp4 -vcodec libx264 -acodec aac -f flv rtmp://test_url

#拉流
ffmpeg -i rtmp://test_url -c copy -t 10 -f mp4 test.mp4
ffmpeg -i rtmp://test_url -c copy -f flv test.flv
#拉流 保存视频片断
ffmpeg  -y -i rtmp://test_url -t 3600 -c copy -flags +global_header -f segment -segment_time 1200 -segment_format_options movflags=+faststart -reset_timestamps 1 test%d.mp4
#拉流 保存图片序列
ffmpeg -y -i rtmp://test_url -r 1 /Users/ludawei/Desktop/2222/out%03d.jpg
#拉流 保存截图
ffmpeg -i rtmp://test_url -y -t 0.001 -ss 1 -f image2 -r 1 test.jpg
#拉流再推流
ffmpeg -i 拉流地址 -acodec copy -vcodec copy -f flv 推流地址

#拉流保存m3u8切片：
ffmpeg -v verbose -i rtmp://test_url -c:v libx264 -c:a aac -ac 1 -strict -2 -crf 20 -profile:v main -maxrate 800k -bufsize 1835k -pix_fmt yuv420p -flags -global_header -hls_time 10 -hls_list_size 6 -start_number 1 -f segment -segment_list ./test/playlist.m3u8 -segment_list_flags +live -segment_time 10 ./test/out%02d.ts
#推本地m3u8文件
ffmpeg -re -i ./test/playlist.m3u8 -vcodec libx264 -acodec aac -preset ultrafast -f flv rtmp://test_url
#视频加水印
ffmpeg -y -i test.mp4 -i watermark.png -filter_complex "overlay=1157:50" test1.mp4

#拉流加水印存4路m3u8
ffmpeg -y -v verbose -i rtmp://test_url -i ./logos/watermark.png -filter_complex "[0:v][1:v]overlay=1157:50,split=4[out1][out2][out3][out4]" -map "[out1]" -c:v libx264 -c:a aac -ac 1 -strict -2 -crf 20 -profile:v main -maxrate 3000k -bufsize 1835k -pix_fmt yuv420p -flags -global_header -hls_time 10 -hls_list_size 6 -start_number 1 -f segment -segment_list ./hls1/playlist.m3u8 -segment_list_flags +live -segment_time 10 ./hls1/out%003d.ts -map "[out2]" -s 1280x720 -c:v libx264 -c:a aac -ac 1 -strict -2 -crf 20 -profile:v main -maxrate 1096k -bufsize 1835k -pix_fmt yuv420p -flags -global_header -hls_time 10 -hls_list_size 6 -start_number 1 -f segment -segment_list ./hls2/playlist.m3u8 -segment_list_flags +live -segment_time 10 ./hls2/out%003d.ts -map "[out3]" -s 640x480 -c:v libx264 -c:a aac -ac 1 -strict -2 -crf 20 -profile:v main -maxrate 564k -bufsize 1835k -pix_fmt yuv420p -flags -global_header -hls_time 10 -hls_list_size 6 -start_number 1 -f segment -segment_list ./hls3/playlist.m3u8 -segment_list_flags +live -segment_time 10 ./hls3/out%003d.ts -map "[out4]" -s 320x180 -c:v libx264 -c:a aac -ac 1 -strict -2 -crf 20 -profile:v main -maxrate 192k -bufsize 1835k -pix_fmt yuv420p -flags -global_header -hls_time 10 -hls_list_size 6 -start_number 1 -f segment -segment_list ./hls4/playlist.m3u8 -segment_list_flags +live -segment_time 10 ./hls4/out%003d.ts

#正常结束录制：
kill -3 进程号
```