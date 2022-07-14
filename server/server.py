import argparse
import socket
import logging
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
    parser.add_argument(
        '--log-file',
        type=str,
        default=None,
        help='File where to store log messages (None = stdout)'
    )
    return parser


def configure_logger(debug, log_file):
    args = {
        'filename': log_file,
        'level': logging.DEBUG if debug else logging.INFO,
        'format': '%(asctime)s %(levelname)-8s %(message)s',
        'datefmt': '%Y-%m-%d %H:%M:%S'
    }
    logging.basicConfig(**args)


def main(host, port, debug, log_file):
    configure_logger(debug, log_file)
    if debug:
        logging.info(f'Running in DEBUG mode --host={host} --port={port}')
        app.run(host=host, port=port)
    else:
        from waitress import serve
        logging.info(f'Running in PRODUCTION mode --host={host} --port={port}')
        serve(app, host=host, port=port)


if __name__ == '__main__':
    opts = get_arg_parser().parse_args()
    main(**vars(opts))
else:
    raise ImportError('This is not a Python Module and it should never be imported!')
