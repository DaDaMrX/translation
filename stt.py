# -*- coding: utf-8 -*-
"""Command line tool for speech to text conversion.

Authors:
    Chengxin Xin [xin.chengxin@foxmail.com]
"""

import argparse
from aip import AipSpeech
    
APP_ID = '15220687'
API_KEY = 'HZffI2RvXSp7H29n6bXo98YW'
SECRET_KEY = 'Dqg1iIt04WBWPSGpmSerPQu0xC6t7rqy'

# read audio file
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def stt(audio_address, target="zh"):
    
    assert target in ['zh', 'en']
    if target == 'zh':
        lang = 1537
    else:
        lang = 1737

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    audio = get_file_content(audio_address)
    res = client.asr(audio, 'wav', 16000, {
            'dev_pid': lang,
    })

    return res['result'][0]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Chinese and English speech to text conversion')
    parser.add_argument('--target', '-t', default='zh', choices=['zh', 'en'],
                        help='Target language (Chinese or English)')
    parser.add_argument('audio_address', 
                        help='Audio to be converted')
    args = parser.parse_args()

    res = stt(args.audio_address, target=args.target)
    print(res)
