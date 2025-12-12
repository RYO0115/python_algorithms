USER_NAME="ramano"
DOCKER_ENV_NAME="python_docker"
VERSION="3.13"

ENV_NAME=${USER_NAME}"/"${DOCKER_ENV_NAME}":"${VERSION}

docker run ${ENV_NAME} --name ${ENV_NAME} -it
            #-v `pwd`:/workspace/python_workspace \
