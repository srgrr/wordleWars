import argparse
import subprocess
import redis
import socket
import logging


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
    parser.add_argument(
        '--redis-port',
        type=int,
        default=6379,
        help='Redis Port'
    )
    parser.add_argument(
        '--redis-insight-port',
        type=int,
        default=8001,
        help='Redis Insight Port'
    )
    parser.add_argument(
        '--words-file',
        type=str,
        default='test_words.txt',
        help='Path to file with words'
    )
    parser.add_argument(
        '--stop-rm-only',
        action='store_true',
        help='Only stop and delete already existing containers'
    )
    parser.add_argument(
        '--schema-only',
        action='store_true',
        help='Only perform create schema'
    )
    return parser.parse_args()


def _create_mysql_schema(mysql_port):
    pass


def _load_words_to_redis(redis_port, words_file):
    redis_client = redis.Redis(
        connection_pool=redis.ConnectionPool(
            host=socket.gethostbyname(socket.gethostname()),
            port=redis_port
        )
    )

    for line in open(words_file):
        line = line.strip()
        x = len(line)
        redis_client.sadd(f'EN-{x}', line)

    sizes = {k: redis_client.scard(k) for k in redis_client.keys('EN-*')}
    logging.debug(f'Number of loaded words per category: {sizes}')


def _configure_logger():
    args = {
        'level': logging.DEBUG,
        'format': '%(asctime)s %(levelname)-8s %(message)s',
        'datefmt': '%Y-%m-%d %H:%M:%S'
    }
    logging.basicConfig(**args)


def main(mysql_port, redis_port, redis_insight_port, words_file, stop_rm_only, schema_only):
    _configure_logger()
    if not schema_only:
      stop_rm_only_val = 'true' if stop_rm_only else 'false'
      logging.warning(f'Calling ./run_db_containers.sh {mysql_port} {redis_port} {redis_insight_port} {stop_rm_only_val}')
      subprocess.call(
        [
          './run_db_containers.sh',
          f'{mysql_port}',
          f'{redis_port}',
          f'{redis_insight_port}',
          stop_rm_only_val
        ]
      )
    if not stop_rm_only:
        logging.debug('Creating MySQL schema...')
        _create_mysql_schema(mysql_port)
        logging.debug('Loading words to Redis...')
        _load_words_to_redis(redis_port, words_file)


if __name__ == '__main__':
    opts = parse_args()
    main(**vars(opts))
else:
    raise ImportError('This is not a Python Module and it should never be imported!')
