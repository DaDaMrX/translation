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

## 文本翻译模块

### 思路
1. 实现了两种文本翻译方案：1）调用Google Translate API进行翻译，2）使用fairseq库训练神经网络模型进行翻译
2. Google Translate API网址：`https://translate.googleapis.com/translate_a/single`, 
可以通过指定参数进行中文到英文到翻译和英文到中文到翻译。（其实可以进行Google Translate支持到所有语言之间到翻译）
3. 训练神经网络模型使用到数据集：WMT17 Chinese-English，网址：`http://www.statmt.org/wmt17/translation-task.html`
4. 使用到的库：pytorch，facebook fairseq：`https://github.com/facebookresearch/fairseq`
5. 模型架构：fconv sequence-to-sequence，参考论文：Convolutional Sequence to Sequence Learning `https://arxiv.org/abs/1705.03122`,
A Convolutional Encoder Model for Neural Machine Translation `https://arxiv.org/abs/1611.02344`


### 接口说明

1. 命令行接口：`python translate.py`，参数：
	1. `--method` 或 `-m`，后面可以跟`api`或`model`，api表示调用google translate api，model表示使用神经网络模型。默认为api。
	2. `--target` 或 `-t`， 后面可以跟`zh`或`en`，zh表示将英文翻译成中文，en表示将中文翻译成英文。默认为zh。
	3. 要进行翻译的文本

2. Python函数接口：在`translate.py`文件中
	1. Google Translate API：`translate_api(text, target)`
	2. 模型：`translate_model(text, target)`
	3. 参数说明：`text`是要翻译的中文或英文字符串，`target`可以是`zh`或`en`。


### 示例

1. 命令行接口
```shell
$ python trainslate.py -m api -t zh "hello"

你好

$ python trainslate.py -m api -t en "你好"

Hello
```

2. Python函数接口
```python
>>> from translate import translate_api, translate_model
>>> text = 'hello'
>>> translate_api(text=text, target='zh')
你好
>>> text = '你好'
>>> translate_model(text=text, target='zh')
Hello
```
