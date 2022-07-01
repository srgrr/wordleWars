#!/bin/bash
set -x

mysql_port=$1
container_name=mysql-5.7-${mysql_port}


# Stop the previous containers
docker stop ${container_name}

# Reset the docker system
docker rm ${container_name}

# MySQL
docker run \
--name ${container_name} \
-d \
-p ${mysql_port}:3306 \
-e MYSQL_ROOT_PASSWORD=root mysql:5.7 \
--character-set-server=utf8 \
--collation-server=utf8_unicode_ci \
--lower-case-table-names=0