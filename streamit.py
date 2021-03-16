import subprocess
import shlex
from os import walk
from random import choice


def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if process.poll() is not None:
            break
        if output:
            print (output.strip())
    rc = process.poll()
    return rc


def list_of_files(path):
    filenames = []
    for (dirpath, _, filespath) in walk(path):
        for filepath in filespath:
            filenames.append(dirpath + '/' + filepath)
    return filenames


def get_random_videofile(path):
    return choice(list_of_files(path))


dir_video = 'video'
stream_key = '17wh-vhr8-5f9q-s9hb-9j6f'
stream_url = 'rtmp://a.rtmp.youtube.com/live2/'

while True:
    videofile = get_random_videofile(dir_video)
    run_command(f'ffmpeg -re -i "{videofile}" -codec: copy -f flv {stream_url}{stream_key}')
