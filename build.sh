USER_NAME="ramano"
DOCKER_ENV_NAME="python_docker"
VERSION="latest"

#ENV_NAME=${USER_NAME}"/"${DOCKER_ENV_NAME}":"${VERSION}
ENV_NAME=${DOCKER_ENV_NAME}


echo ${ENV_NAME}
docker build --tag ${ENV_NAME} .