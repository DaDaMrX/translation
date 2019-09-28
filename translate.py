# -*- coding: utf-8 -*-
"""Command line tool for translating text between English and Chinese.

Authors:
    Heng-Da Xu <dadamrxx@gmail.com>
"""
import argparse
import re
import subprocess

import requests


def translate_api(text, target):
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


def translate_model(text, target):
    assert target in ['zh', 'en']
    if target == 'zh':
        source = 'en'
        model_path = 'model/en2zh.pt'
    else:
        source = 'zh'
        model_path = 'model/zh2en.pt'
    cmd = (f'fairseq-interactive model '
           f'--source-lang {source} --target-lang {target} '
           f'--path {model_path} '
           f'--beam 10 --remove-bpe --cpu')
    output = subprocess.run(
            cmd, input=text,
            shell=True, check=True, 
            capture_output=True, text=True
    ).stdout
    res = re.search(r'H-\d+\s+.+?\s+(.+)', output).group(1)
    if target == 'zh':
        res = re.sub(r'\s+', '', res)
    return res


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Translate text between English and Chinese.')
    parser.add_argument('--method', '-m', choices=['api', 'model'], default='api',
                        help='Which method to use (Google API or NN model)')
    parser.add_argument('--target', '-t', choices=['zh', 'en'], default='zh',
                        help='Target language (Chinese or English)')
    parser.add_argument('text', 
                        help='Text to be translated')
    args = parser.parse_args()

    if args.method == 'api':
        res = translate_api(args.text, target=args.target)
    else:
        res = translate_model(args.text, target=args.target)
    print(res)
