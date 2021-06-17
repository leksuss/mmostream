# StreamIt

[![Maintainability](https://api.codeclimate.com/v1/badges/a071a3e9a96bad8d1cf2/maintainability)](https://codeclimate.com/github/leksuss/streamit/maintainability)

This tool is for creating a stream for youtube broadcasting. Suppose you have a directory with video files and want to stream this files with youtube broadcasting: randomly and looply. If so, you find what you need!


StreamIt is very simple and lightweight. Videofiles used as is with no live conversion. Therefore there is no load on CPU and you can use any VDS/VPS with minimum CPU/RAM, but with decent HDD/SSD and outbound bandwidth.

### Requirements
* python 3
* tmux (optional)

### How to use

To start streaming you need to specify folder with video files, stream key and stream url. You can find it on Dashboard livestream on your youtube account:

<img width="700" alt="youtube_stream" src="https://user-images.githubusercontent.com/11560975/112851450-a82d0300-90b3-11eb-819b-3cf5f0877c13.png">

And use it like this (default url is `rtmp://a.rtmp.youtube.com/live2`):

> python3 streamit.py /home/user/folder_with_videos --key 90b3-11eb-819b-3cf5f0877


This is runtime tool, so the better way is run it inside **tmux**, **screen** or something.

### Bonus: converting script

If you received a bad keyframe message from youtube broadcast service, you need to convert videofiles with to force key frame every 2-3 seconds. See [ffmpeg documentation](https://ffmpeg.org/ffmpeg.html) for all the functions and their details. You can use `convert.py` script to do this. Just set `path` and `dest_path` to specify source/dest dir with video files. 
