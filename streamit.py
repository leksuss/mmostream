from os import walk
from random import choice
import subprocess
import shlex
import time

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
    command = f'ffmpeg -re -i "{file}" -codec: copy -f flv -flvflags no_duration_filesize {url}/{key}'
    return command


def streamit(args):
    print(f'Playing random video file from path: {args.path}')
    print(f'Sendign stream to url: {args.url}/{args.key}')
    print()
    timer = time.time()
    while True:
        if args.break_every is not None and time.time() - timer > args.break_every:
            print(f'Going to sleep {args.break_timeout} seconds')
            time.sleep(args.break_timeout)
            timer = time.time()
        videofile = get_random_videofile(args.path)
        run_command(gen_command_string(videofile, args.url, args.key))


if __name__ == '__main__':
    args = get_cli_args()
    streamit(args)
