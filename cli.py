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

    return parser.parse_args()
