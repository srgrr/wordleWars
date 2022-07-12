import argparse
import subprocess
import redis
import socket


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
    # words_file = ("test_words.txt")
    for line in open("test_words.txt"):
        line = line.strip()
        x = len(line)
        redis_client.sadd(f'EN-{x}', line)

    # you should see this entry using redisInsight
    # redis_client.rpush('key', 'value1')
    # redis_client.rpush('key', 'value2')


def main(mysql_port, redis_port, redis_insight_port, words_file):
    subprocess.call(
        [
            './run_db_containers.sh',
            f'{mysql_port}',
            f'{redis_port}',
            f'{redis_insight_port}'
        ]
    )
    _create_mysql_schema(mysql_port)
    _load_words_to_redis(redis_port, words_file)


if __name__ == '__main__':
    opts = parse_args()
    main(**vars(opts))