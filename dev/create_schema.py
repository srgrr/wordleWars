import argparse
import subprocess


def parse_args():
    parser = argparse.ArgumentParser(
        'Setup a local environment for testing purposes'
    )
    parser.add_argument(
        '--mysql-port',
        type=int,
        default=3306,
        help='MySQL Port'
    )
    return parser.parse_args()


def main(mysql_port):
    subprocess.call(
        [
            './run_db_containers.sh',
            f'{mysql_port}'
        ]
    )


if __name__ == '__main__':
    opts = parse_args()
    main(**vars(opts))