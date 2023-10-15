import argparse
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
from datetime import date

today = date.today()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path')
    args = parser.parse_args()
    wav_file = args.path
    dir_name = os.path.dirname(args.path)
    dirs = dir_name.split('/')

    speech = AudioSegment.from_wav(wav_file)
    # min_silence_len: how long is the silence? 
    # silence_thresh: how much volume is the silence?
    # keep_silence: add silence to each cutted wav
    chunks = split_on_silence(speech, min_silence_len=600, silence_thresh=-40, keep_silence=300, seek_step=100)
    for i in range(0, len(chunks)):
        chunks[i].export("%s/%s%03d.wav" % (dir_name, f'5_3039_{today.strftime("%Y%m%d")}', i), format='wav', parameters=["-ar", "16000", "-ac", "1"])

if __name__ == '__main__':
    main()
