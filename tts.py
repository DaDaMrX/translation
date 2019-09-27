# -*- coding: utf-8 -*-
"""Command line tool for text to speech conversion.

Authors:
    Chengxin Xin [xin.chengxin@foxmail.com]
"""

from aip import AipSpeech

APP_ID = '15220687'
API_KEY = 'HZffI2RvXSp7H29n6bXo98YW'
SECRET_KEY = 'Dqg1iIt04WBWPSGpmSerPQu0xC6t7rqy'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result  = client.synthesis('你好,信息检索', 'zh', 1, {
    'vol': 5,
})

if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)