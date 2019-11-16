# 系统说明书
## 视频字幕提取系统
### 思路
1. 首先通过moviepy模块，将视频中的音频进行提取。
2. 接着使用pydub模块，对音频进行分割，得到单独的每句话，以及其对应的时间轴。
3. 通过百度的语音识别API，对分割出的每句话进行识别处理，得到对应文字。
4. 将时间轴、字幕文件进行组合，输出到对应srt文件中，得到字幕文件。

### 使用方法
1. 视频字幕提取：运行vtt.py文件，参数：
	1. --video_address 表示需要进行字幕提取的课程视频，
	2. --target 表示视频所使用的语言，我们的程序支持英文与中文(‘en’，‘zh’)两种语言的字幕转换。 
	3. --output_file 表示目标srt文件名。
2. 视频音频提取：运行vts.py文件，参数：
	1. --video_address 表示需要进行音频提取的课程视频
	2. --target_address 表示目标音频文件。
3. 音频字幕转换：运行stt.py文件，参数：
	1. --target 表示视频所使用的语言，我们的程序支持英文与中文(‘en’，‘zh’)两种语言的字幕转换。 
	2. audio_address 表示目标音频文件名称。

	
### 示例
```
➜  translation git:(master) ✗ python vtt.py --video_address=video.mp4 -t='en' --output_file=out.srt
MoviePy - Writing audio in %s
MoviePy - Done.
总分段： 169
取有效分段(大于2s小于10s)： 162
1
0:00:00,0 --> 0:00:03,0
here are those six topic areas again
2
0:00:03,0 --> 0:00:08,0
I am describing activity is the fifth one in this series of lessons
```