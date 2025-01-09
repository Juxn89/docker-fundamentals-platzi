# Docker fundamentals by **Platzi**
## Docs
- [https://hub.docker.com/](https://hub.docker.com/)
- [Docker images](https://hub.docker.com/?search?q=)

## Basic commands
### General comamds
- Get Docker version: ```docker --version```
- Get Docker documentation: ```docker``` or ```docker help```
- Get Docker information: ```docker info```, show information related to hardward

### Images commands
- Get Docker images: ```docker images```, show all images created or ```docker images IMAGE_NAME```
	or ```docker images --filter=reference='*:CRITERIA'```
	- ```docker images website```
	- ```docker images --filter=reference='*:latest'```, other: ```docker images --filter=reference=`*:1.0```
- Get Docker images with real **IMAGE ID**: ```docker images --no-trunc```
- **UPDATE** tag or name of a docker image: ```docker image tag IMAGE_NAME:NAME_TAG NEW_IMAGE_NAME:NEW_IMAGE_TAG```
	- ```docker image tag website:latest jgomez/website:latest```
- Delete a image: ```docker rmi -f IMAGE_ID``` or ```docker rmi IMAGE_NAME```
	- **rmi**: means **remove image**
	- **-f**: means **force**

### Container commands
- Get Docker containers: ```docker ps```, show all containers
	- Add the size of the container: ```docker ps --size```
- Stop a container: ```docker stop CONTAINER_ID```

### Others
- Build: ```docker build```
- Run: ```docker run```
- Build a image with name and tag: ```docker build -t NAME:TAG .```
	- ```docker build -t website:latest .```

## Avanced commands
- Run a container: ```docker -it --rm -d -p LOCAL_PORT:IMAGE_PORT --name CUSTOM_NAME_CONTAINER NAME_IMAGE```
	- ```docker run -it --rm -d -p 8080:80 --name web website```
	- ```docker run -it --rm -d -p 8080:80 --name web website:1.0``` or ```docker run -it --rm -d -p 8080:80 --name web website:latest```
- Run a container with volumen: ```docker -it --rm -d -p -v ./LOCAL_FOLDER:CONTAINER_FOLDER LOCAL_PORT:IMAGE_PORT --name CUSTOM_NAME_CONTAINER NAME_IMAGE```
	- ```docker run -it --rm -d -p 8080:80 ./site:/usr/share/nginx/html/site --name web website:1.0```
	```docker
	FROM nginx:latest

	COPY /site	/usr/share/nginx/html

	VOLUME ["/site", "/usr/share/nginx/html"]
	```
- Show networks in docker: ```docker network ls```
- Create a network in docker: ```docker network create NETWORK_NAME```
- Share a image with Docker Hub: ```docker push IMAGE_NAME```
	- Before, you must log in using the command: ```docker login```
- Save and recovery a docker image:
	- **Save**: ```docker save IMAGE_NAME > CUSTOM_NAME.rar```
	- **Restore**: ```docker load --input CUSTOM_NAME.rar```

## Docker Compose
### Commands
- Build: ```docker compose build```
- Run: ```docker compose run```

## Workflow
- Docker file **build** Docker image **run** Docker container