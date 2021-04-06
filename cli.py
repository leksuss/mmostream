import argparse


def get_cli_args():
    """Parse args from cli"""
    parser = argparse.ArgumentParser(
        prog='streamit',
        description='Stream videofiles to Youtube',
    )
    parser.add_argument(
        'path',
        type=str,
        default='video',
        help='folder with videofiles',
    )
    parser.add_argument(
        '-k',
        '--key',
        type=str,
        required=True,
        help='youtube stream key',
    )
    parser.add_argument(
        '-u',
        '--url',
        type=str,
        default='rtmp://a.rtmp.youtube.com/live2',
        help='youtube stream url',
    )
    parser.add_argument(
        '-b',
        '--break_every',
        type=int,
        help='Break stream every x seconds',
    )
    parser.add_argument(
        '-t',
        '--break_timeout',
        type=int,
        default=3,
        help='Delay in seconds between streams which are created by --break_every key',
    )
    return parser.parse_args()

