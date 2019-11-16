# -*- coding: utf-8 -*-
"""Command line tool for video to speech conversion.

Authors:
    Yu Bai [wnwhiteby@gmail.com]
"""

import argparse
import path
from moviepy.editor import *


def videoToSpeech(source, target):
    """提取视频的音频文件

    参数
    ----------
    source : str
        源文件地址
    target : str
        目标文件输出地址
    """

    video = VideoFileClip(source)
    audio = video.audio
    audio.write_audiofile(target)
    return 



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Video to speech')
    parser.add_argument('--video_address', 
                        type=str,
                        action='store',
                        # default='test.mp4',
                        help='video to be converted(mp4)')
    parser.add_argument('--target_address', 
                        type=str,
                        action='store',
                        # default='target.wav',
                        help='target address')

    args = parser.parse_args()

    videoToSpeech(args.video_address, target=args.target_address)
    print("Convert finished!")

