import path
import os
from moviepy.editor import *
import argparse
from aip import AipSpeech
from pydub import AudioSegment
from vts import videoToSpeech
from stt import stt
from speech_split import speech_split




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

    args = parser.parse_args()

    videoToSpeech(args.video_address, target="tmp.wav")
    # res = stt("tmp.wav", target=args.target)
    os.makedirs("splits")
    chunks, chunk_lens = speech_split("tmp.wav", "splits")
    # chunks = os.listdir("splits")
    for i, each in enumerate(chunks):
        # print(each)
        print(str(chunk_lens[i][0]) + " ~ " + str(chunk_lens[i][1]), end=': ')
        print(stt("splits/"+ each, args.target))
        os.remove("splits/" + each)
    os.remove("tmp.wav")
    os.removedirs("splits")
