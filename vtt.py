# -*- coding: utf-8 -*-
"""Command line tool for video to text conversion.

Authors:
    Yu Bai [wnwhiteby@gmail.com]
"""

import path
import os
from moviepy.editor import *
import argparse
from aip import AipSpeech
from pydub import AudioSegment
from vts import videoToSpeech
from stt import stt
from speech_split import speech_split


def convert_time(seconds):
    """在这里写函数的一句话总结(如: 计算平均值).

    这里是具体描述.

    参数
    ----------
    seconds : int
        需要被转换的秒数 

    返回值
    -------
    str 
        转换完成的时间字符串。
    """
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)


def process(args):
    """对视频文件进行提取字幕操作。

    参数
    ----------
    --video_address : str
        视频地址
    --target : str
        目标语言
   --output_file : str
        输出地址
    """
    videoToSpeech(args.video_address, target="tmp.wav")
    # res = stt("tmp.wav", target=args.target)
    os.makedirs("splits")
    chunks, chunk_lens = speech_split("tmp.wav", "splits")
    # chunks = os.listdir("splits")
    lastend = 0
    res = ""
    for i, each in enumerate(chunks):
        # print(each)
        # print(str(chunk_lens[i][0]) + " ~ " + str(chunk_lens[i][1]), end=': ')
        starttime=convert_time(max(int(chunk_lens[i][0]), lastend))
        endtime = convert_time(int(chunk_lens[i][1]))
        lastend = int(chunk_lens[i][1])
        # print(str(starttime)+ ",0 --> " + str(endtime) + ",0 " +  stt("splits/"+ each, args.target))
        tmp = str(i+1) + "\n" + str(starttime)+ ",0 --> " + str(endtime) + ",0 \n" +  stt("splits/"+ each, args.target)
        res += (tmp + '\n\n')
        print(tmp)
        # print(stt("splits/"+ each, args.target))
        os.remove("splits/" + each)
    with open(args.output_file,'w') as f:    #设置文件对象
        f.write(res)                 #将字符串写入文件中
    os.remove("tmp.wav")
    os.removedirs("splits")
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Video to speech')
    parser.add_argument('--video_address', 
                        type=str,
                        action='store',
                        # default='test.mp4',
                        help='video to be converted(mp4)')
    parser.add_argument('--target', '-t', default='zh', choices=['zh', 'en'],
                        help='Target language (Chinese or English)')

    parser.add_argument('--output_file', 
                    type=str,
                    action='store',
                    default='out.srt',
                    help='output file address')
    args = parser.parse_args()
    process(args)

