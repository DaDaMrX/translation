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

- [x] Speech-to-text with API  
- [x] Video-to-speech
- [ ] Speech-to-text with model
