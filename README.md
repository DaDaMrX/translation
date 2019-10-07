# Translation and Speech-to-text 

Translation and Speech-to-text component of the final project in Information Retrieval course 2019 in BIT.

## Members

- Heng-Da Xu [dadamrxx@gmail.com](dadamrxx@gmail.com)
- Jia-Nan Guo [guojn97@gamil.com](guojn97@gamil.com)
- Yu Bai [wnwhiteby@gmail.com](wnwhiteby@gmail.com)
- Chengxin Xin [xin.chengxin@foxmail.com](https://github.com/fihxc)
- Shuyang Lin [linshuyang2017@gmail.com](linshuyang2017@gmail.com)

## Translation

### Translate by Google Translate API

- Make sure you can access Google first.

Usage:
```shell
$ python trainslate.py -m api -t zh "hello"

你好

$ python trainslate.py -m api -t en "你好"

Hello
```

### Translate by NN model

- lease download the pretrained model from [here](https://drive.google.com/uc?id=1D2QGRxHyAIJoJGsDlF7LgpfuDxOrnfuU&export=download).

- Unzip the file to the root directory.

- Make sure you have installed [fairseq](https://github.com/pytorch/fairseq) and [PyTorch](https://pytorch.org).

Usage:
```shell
$ python trainslate.py -m model -t zh "hello"

$ python trainslate.py -m model -t en "你好"
```

Reference: [https://github.com/twairball/fairseq-zh-en](https://github.com/twairball/fairseq-zh-en)

## Speech-to-text

Usage:
```shell
$ python stt.py -t zh stt_audio.wav

啊啊啊。
```
```shell
$ python vtt.py --video_address=video.mp4 -t='en'

MoviePy - Writing audio in %s
MoviePy - Done.
总分段： 184
取有效分段(大于2s小于10s)： 137
0.0 ~ 3.047: here are those six topic areas again
2.771 ~ 8.289: I'm describing activity is the fifth one in this series of lessons
8.103 ~ 10.145: let's look at this topic now
10.208 ~ 15.356: when your asked to describe an activity I think this is quite an easy topic
15.1 ~ 19.807: but we still have to prepare some good vocabulary for it so that we're ready
```

- [x] Speech-to-text with API  
- [x] Video-to-speech with API
- [x] Video-to-text with API
- [ ] generate srt file
- [ ] Speech-to-text with model
