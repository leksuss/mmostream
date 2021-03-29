import subprocess
import shlex
from os import walk
from random import choice
from cli import get_cli_args


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


def gen_command_string(file, url, key):
    command = f'ffmpeg -re -i "{file}" -codec: copy -f flv {url}/{key}'
    return command


def streamit(dir_video, stream_url, stream_key):
    print(f'Playing random video file from path: {dir_video}')
    print(f'Sendign stream to url: {stream_url}/{stream_key}')
    print()
    while True:
        videofile = get_random_videofile(dir_video)
        run_command(gen_command_string(videofile, stream_url, stream_key))


if __name__ == '__main__':
    args = get_cli_args()
    streamit(args.path, args.url, args.key)
