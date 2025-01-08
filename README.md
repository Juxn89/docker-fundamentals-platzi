# Docker fundamentals by **Platzi**
## Docs
- [https://hub.docker.com/](https://hub.docker.com/)
- [Docker images](https://hub.docker.com/?search?q=)

## Basic commands
- Get Docker version: ```docker --version```
- Get Docker documentation: ```docker``` or ```docker help```
- Get Docker information: ```docker info```, show information related to hardward
- Get Docker images: ```docker images```, show all images created or ```docker images IMAGE_NAME```
	or ```docker images --filter=reference='*:CRITERIA'```
	- ```docker images website```
	- ```docker images --filter=reference='*:latest'```, other: ```docker images --filter=reference=`*:1.0```
- Get Docker images with real **IMAGE ID**: ```docker images --no-trunc```
- **UPDATE** tag or name of a docker image: ```docker image tag IMAGE_NAME:NAME_TAG NEW_IMAGE_NAME:NEW_IMAGE_TAG```
	- ```docker image tag website:latest jgomez/website:latest```
- Get Docker containers: ```docker ps```, show all containers
- Build: ```docker build```
- Run: ```docker run```
- Delete a image: ```docker rmi -f IMAGE_ID``` or ```docker rmi IMAGE_NAME```
	- **rmi**: means **remove image**
	- **-f**: means **force**
- Build a image with name and tag: ```docker build -t NAME:TAG .```
	- ```docker build -t website:latest .```

## Avanced commands
- Run a container: ```docker -it -rm -d -p LOCAL_PORT:IMAGE_PORT --name CUSTOM_NAME_CONTAINER NAME_IMAGE```
	- ```docker run -it --rm -d -p 8080:80 --name web website```

## Workflow
- Docker file **build** Docker image **run** Docker container