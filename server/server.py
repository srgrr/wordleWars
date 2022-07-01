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
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Enable debug mode'
    )
    return parser


def main(host, port, debug):
    if debug:
        app.run(host=host, port=port)
    else:
        from waitress import serve
        serve(app, host=host, port=port)


if __name__ == '__main__':
    opts = get_arg_parser().parse_args()
    main(**vars(opts))
