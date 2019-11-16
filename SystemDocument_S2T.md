# 系统说明书

## 实验目的

随着互联网的快速发展，使得网络视频的内容越来越丰富，包涵着越来越多的重要信息，大量的视频图像在网络上快速传播，网络视频的服务更快、更便捷，但也增加了对视频内容进行检索的难度。

因此，对视频的检索成为了当今计算机领域研究的热点和难点。视频字幕被用于显示人物的对话，背景信息的介绍等，是视频内容的直接反映，与视频内容密切相关，是理解视频内容的重要而准确的线索。如果能够实现对视频中字幕的检测和提取，就可以很好的理解和分析视频内容，从而实现对网络视频进行检索，也有助于对视频字幕进行翻译。

传统的基于关键词、标题的方法，一般采用人工方式进行编写，不仅效率低而且并不能准确的反映视频内容，要从海量的视频数据中快速、准确地查找所需要的视频信息，需要理解视频的内容。视频字幕包含了丰富的高层语义信息，与视频语义有很强的相关性，是理解视频内容的重要线索。因此, .从网络视频中自动检测、提取视频字幕能够对视频进行更深入的检索与理解，也可对视频字幕进行高效率的翻译，将大大提升工作效率，节省人力。   

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

## 视频中英文字幕生成

### 思路

1.文本翻译模块提供文本翻译接口，供视频字幕提取系统调用

2.视频字幕提取系统进行修改，增加“是否翻译”的选项

### 接口说明

视频字幕提取：运行vtt.py文件，参数：

1. --video_address 表示需要进行字幕提取的课程视频，
2. --target 表示视频所使用的语言，我们的程序支持英文与中文(‘en’，‘zh’)两种语言的字幕转换。 
3. --output_file 表示目标srt文件名。
4. --translate 表示对字幕进行翻译，生成双语字幕（自动识别源语言并进行翻译，即英文转中文，中文转英文）。

### 示例

```sh
$ python vtt.py \
    --video_address=video_english.mp4 \
    -t='en' \
    --output_file=out1.srt \
    --translate

MoviePy - Writing audio in tmp.wav
MoviePy - Done.                                                                                                    
总分段： 23
取有效分段(大于2s小于10s)： 21
1
0:00:00,0 --> 0:00:03,0 
here are those six topic areas again
这又是这六个主题领域
2
0:00:03,0 --> 0:00:08,0 
I am describing activity is the fifth one in this series of lessons
我描述的活动是本系列课程的第五部分
3
0:00:08,0 --> 0:00:10,0 
let's look at this topic now
让我们现在来看这个话题
...
```