"""
avi2jpg.py

convert .avi recordings into .jpg images

Jan. 19, 2021
"""
import subprocess, argparse
from glob import glob

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_avi')
    args = parser.parse_args()
    return args

def main(args):
    input_avi = args.input_avi
    base_name = input_avi.split('.')[:-1][0]
    print(base_name)
    subprocess.call(['ffmpeg','-i',input_avi,'-f','image2',base_name+'_frame-%06d.jpg'])

if __name__ == '__main__':
    args = get_args()
    main(args)
