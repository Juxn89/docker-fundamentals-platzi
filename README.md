# Docker fundamentals by **Platzi**
## Docs
- [https://hub.docker.com/](https://hub.docker.com/)
- [Docker images](https://hub.docker.com/?search?q=)

## Basic commands
- Get Docker version: ```docker --version```
- Get Docker documentation: ```docker``` or ```docker help```
- Get Docker information: ```docker info```, show information related to hardward
- Get Docker images: ```docker images```, show all images created
- Get Docker containers: ```docker ps```, show all containers
- Build: ```docker build```
- Run: ```docker run```
- Delete a image: ```docker rmi -f IMAGE_ID```
- Build a image with name and tag: ```docker build -t NAME:TAG .```
	- ```docker build -t website:latest .```

## Avanced commands
- Run a container: ```docker -it -rm -d -p LOCAL_PORT:IMAGE_PORT --name CUSTOM_NAME_CONTAINER NAME_IMAGE```
	- ```docker run -it --rm -d -p 8080:80 --name web website```

## Workflow
- Docker file **build** Docker image **run** Docker container