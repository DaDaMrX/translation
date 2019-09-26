# -*- coding: utf-8 -*-
"""Command line tool for translating text between English and Chinese.

Authors:
    Heng-Da Xu <dadamrxx@gmail.com>
"""

import argparse

import requests


def translate(text, target='zh'):
    assert target in ['zh', 'en']
    if target == 'zh':
        source, target = 'en', 'zh'
    else:
        source, target = 'zh', 'en'
    url = 'https://translate.googleapis.com/translate_a/single'
    params = {
        'client': 'gtx',
        'sl': source,
        'tl': target,
        'dt': 't',
        'q': text,
    }
    res = requests.get(url, params=params).text
    res = eval(res.replace('null', "'null'"))[0][0][0]
    return res


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Translate text between English and Chinese.')
    parser.add_argument('--target', '-t', default='zh', choices=['zh', 'en'],
                        help='Target language (Chinese or English)')
    parser.add_argument('text', 
                        help='Text to be translated')
    args = parser.parse_args()

    res = translate(args.text, target=args.target)
    print(res)