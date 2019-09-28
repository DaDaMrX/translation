# Translation and Speech-to-text 

Translation and Speech-to-text component of the final project in Information Retrieval course 2019 in BIT.

## Members

- Heng-Da Xu [dadamrxx@gmail.com](dadamrxx@gmail.com)
- Jia-Nan Guo [guojn97@gamil.com](guojn97@gamil.com)
- Yu Bo
- Chengxin Xin
- Shuyang Lin

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

- lease download the pretrained model from [here](https://drive.google.com/uc?id=12UK2evibWAWwIkqKhvyfGsFD-ImrJ6Hn&export=download).

- Unzip the file to the root directory.

- Make sure you have installed [fairseq](https://github.com/pytorch/fairseq) and [PyTorch](https://pytorch.org).

Usage:
```shell
$ python trainslate.py -m model -t zh "hello"

$ python trainslate.py -m model -t en "你好"
```

Reference: [https://github.com/twairball/fairseq-zh-en](https://github.com/twairball/fairseq-zh-en)

## Speech-to-text

- [ ] Speech-to-text with API  
- [ ] Speech-to-text with model
