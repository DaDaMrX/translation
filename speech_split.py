# -*- coding: utf-8 -*-
"""Command line tool for speech split

Authors:
    Yu Bai [wnwhiteby@gmail.com]
"""
import argparse
from pydub import AudioSegment
from pydub.silence import detect_nonsilent
 

def split_on_silence(audio_segment, min_silence_len=1000, silence_thresh=-16, keep_silence=100,
                     seek_step=1):
    """
    audio_segment - original pydub.AudioSegment() object

    min_silence_len - (in ms) minimum length of a silence to be used for
        a split. default: 1000ms

    silence_thresh - (in dBFS) anything quieter than this will be
        considered silence. default: -16dBFS

    keep_silence - (in ms) amount of silence to leave at the beginning
        and end of the chunks. Keeps the sound from sounding like it is
        abruptly cut off. (default: 100ms)
    """

    not_silence_ranges = detect_nonsilent(audio_segment, min_silence_len, silence_thresh, seek_step)

    chunks = []
    starttime = []
    endtime = []
    for start_i, end_i in not_silence_ranges:
        start_i = max(0, start_i - keep_silence)
        end_i += keep_silence

        chunks.append(audio_segment[start_i:end_i])
        starttime.append(start_i)
        endtime.append(end_i)

    return chunks, starttime, endtime

def speech_split(speech_file, save_dir):
    """ 音频分割，并得到其时间轴位置

    参数
    ----------
    speech_file : str
        音频文件地址
    save_dir : str
        保存文件地址

    返回值
    -------
    chunkss
        分割音频文件地址
    chunk_lens
        音频起止时间

    """
    sound = AudioSegment.from_mp3(speech_file)
    loudness = sound.dBFS
    #print(loudness)
    
    chunks, starttime, endtime = split_on_silence(sound,
        # must be silent for at least half a second,沉默半秒
        min_silence_len=350,
    
        # consider it silent if quieter than -16 dBFS
        silence_thresh=-45,
        keep_silence=400
    
    )
    print('总分段：', len(chunks))
    chunk_lens = []
    for i, chunk in enumerate(chunks):
        chunk_lens.append((starttime[i]/ 1000, endtime[i] / 1000))

    
    # 放弃长度小于2秒的录音片段
    for i in list(range(len(chunks)))[::-1]:
        if len(chunks[i]) <= 1500 or len(chunks[i]) >= 10000:
            chunks.pop(i)
            chunk_lens.pop(i)
    print('取有效分段(大于2s小于10s)：', len(chunks))
    
    '''
    for x in range(0,int(len(sound)/1000)):
        print(x,sound[x*1000:(x+1)*1000].max_dBFS)
    '''
    
    chunkss = []
    for i, chunk in enumerate(chunks):
        chunk.export(save_dir + "/chunk{0}.wav".format(i), format="wav")
        chunkss.append("/chunk{0}.wav".format(i))
    
    return chunkss, chunk_lens

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Video to speech')
    parser.add_argument('--speech_address', 
                        type=str,
                        action='store',
                        # default='test.mp4',
                        help='video to be converted(mp4)')
    parser.add_argument('--save_dir', 
                        type=str,
                        action='store',
                        # default='test.mp4',
                        help='video to be converted(mp4)')
 
    args = parser.parse_args()
    _ = speech_split(args.speech_address, args.save_dir)
