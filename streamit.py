import os
import subprocess
import shlex
from os import walk
from random import choice
import sys

def sh(cmd, input=""):

    rst = subprocess.run(cmd,
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         text=True,
                         check=True,
                         )
    assert rst.returncode == 0, rst.stderr
    return rst.stdout.strip()


def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print (output.strip())
    rc = process.poll()
    return rc


def run(command):
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True,
        encoding='utf-8',
        errors='replace',

    )

    while True:
        realtime_output = process.stdout.readline()
        if realtime_output == '' and process.poll() is not None:
            break

        if realtime_output:
            print(realtime_output.strip(), flush=True)
    return process.poll()


def _run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True)
    if result.stderr:
        raise subprocess.CalledProcessError(
                returncode = result.returncode,
                cmd = result.args,
                stderr = result.stderr
                )

    if result.stdout:
        print("Command Result: {}".format(result.stdout.decode('utf-8')))
    return result


def list_of_files(path):
    filenames = []
    for (dirpath, _, filespath) in walk(path):
        for filepath in filespath:
            filenames.append(dirpath + '/' + filepath)
    return filenames


def get_random_videofile(path):
    return choice(list_of_files(path))

dir_video = 'video'
stream_key = '7x0u-9fxt-dd6s-gycq-8hsr'
stream_url = 'rtmp://a.rtmp.youtube.com/live2/'

count_of_tries = 0
while True:
    videofile = get_random_videofile(dir_video)
    try:
        # _run_command(f'python -c "print(\'wow!\')"')
        # _run_command(f'python -c "raise ValueError(\'oops\')"')
        _run_command(f'ffmpeg -re -i "{videofile}" -codec: copy -f flv {stream_url}{stream_key}')
    except subprocess.CalledProcessError as error:
        print(error.stderr)
        count_of_tries += 1
        if count_of_tries:
            print(f"Can't continue stream, too many tries: {count_of_tries}")
            break
