# -*- coding: utf-8 -*-
"""Command line tool for speech to text conversion.

Authors:
    Chengxin Xin [xin.chengxin@foxmail.com]
"""

from aip import AipSpeech

APP_ID = '15220687'
API_KEY = 'HZffI2RvXSp7H29n6bXo98YW'
SECRET_KEY = 'Dqg1iIt04WBWPSGpmSerPQu0xC6t7rqy'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# read audio file
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

res = client.asr(get_file_content('stt_audio.wav'), 'wav', 16000, {
    'dev_pid': 1537,
})

print(res)