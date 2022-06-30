import argparse
import socket
from rest import app


def get_arg_parser():
    parser = argparse.ArgumentParser('Start the wordleWars server!')
    parser.add_argument(
        '--host',
        type=str,
        default=socket.gethostbyname(socket.gethostname()),
        help='Server host'
    )
    parser.add_argument(
        '--port',
        type=int,
        default=5000,
        help='Server port'
    )
    return parser


def main(host, port):
    app.run(host=host, port=port)


if __name__ == '__main__':
    opts = get_arg_parser().parse_args()
    main(**vars(opts))
