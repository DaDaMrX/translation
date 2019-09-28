# -*- coding: utf-8 -*-
"""Command line tool for video to speech conversion.

Authors:
    Yu Bai [wnwhiteby@gmail.com]
"""

import argparse
import path
from moviepy.editor import *


def videoToSpeech(source, target):
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

