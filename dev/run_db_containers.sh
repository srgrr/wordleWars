#!/bin/bash
set -x

# MySQL params
mysql_port=$1
mysql_container_name=mysql-5.7-${mysql_port}

# Redis params
redis_port=$2
redis_insight_port=$3
redis_container_name=redis-stack-${redis_port}-${redis_insight_port}

# Stop the previous containers
docker stop ${mysql_container_name}
docker stop ${redis_container_name}

# Reset the docker system
docker rm ${mysql_container_name}
docker rm ${redis_container_name}

# MySQL
docker run \
--name ${mysql_container_name} \
-d \
-p ${mysql_port}:3306 \
-e MYSQL_ROOT_PASSWORD=root mysql:5.7 \
--character-set-server=utf8 \
--collation-server=utf8_unicode_ci \
--lower-case-table-names=0

# Redis
docker run \
-d --name ${redis_container_name} \
-p ${redis_port}:${redis_port} \
-p ${redis_insight_port}:${redis_insight_port} \
redis/redis-stack:latest

# TODO CREATE MYSQL SCHEMA
