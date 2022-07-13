---
type: post
title: Docker Cheat Sheet
subtitle: 
thumbnail-img: ""
share-img: /assets/img/path.jpg
tags: [Docker]
---
Command | Description
:--- | :---
docker ps | 查看当前运行中的容器
docker images | 查看镜像列表
docker rm container-id | 删除指定 id 的容器
docker stop/start container-id | 停止/启动指定 id 的容器
docker rmi image-id | 删除指定 id 的镜像
docker volume ls | 查看 volume 列表
docker network ls | 查看网络列表

Docker Compose

Command | Description
:--- | :---
在后台运行只需要加一个 -d | 参数docker-compose up -d
查看运行状态：| docker-compose ps
停止运行：| docker-compose stop
重启：| docker-compose restart
重启单个服务：| docker-compose restart service-name
进入容器命令行：| docker-compose exec service-name sh
查看容器运行log：| docker-compose logs [service-name]