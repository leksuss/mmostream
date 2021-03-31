import subprocess
import shlex
import os

path = 'video'
dest_path = 'video1'


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


def unconverted_files(path, dest_path):
    filenames = set()
    for (dirpath, _, filespath) in os.walk(path):
        for filepath in filespath:
            if filepath.endswith('.mp4'):
                filenames.add(filepath)

    filenames_converted = set()
    for (dirpath, _, filespath) in os.walk(dest_path):
        for filepath in filespath:
            if filepath.endswith('.mp4'):
                filenames_converted.add(filepath)

    return filenames - filenames_converted


def gen_command_string(file, out_file):
    command = f'ffmpeg -i "{file}" -c:v libx264 -tune animation -preset veryslow -c:a copy -force_key_frames "expr:gte (t, n_forced * 2)" -f mp4 "{out_file}"'
    return command


if __name__ == '__main__':
    files = unconverted_files(path, dest_path)
    while files:
        file = next(iter(files))
        source_file = os.path.join(path, file)
        dest_file = os.path.join(dest_path, file)
        run_command(gen_command_string(source_file, dest_file))
        files = unconverted_files(path, dest_path)
