#!/bin/bash

set -e

# Path to the directory containing the Dockerfile
DOCKERFILE_PATH="/Users/tim/Desktop/Projekte/OpenQA/openqa/api/setup_env/setup_crew"

# Build the Docker image
docker build -t app_env:latest $DOCKERFILE_PATH

# Run a container and install a library
CONTAINER_ID=$(docker run -d app_env:latest /bin/sh -c "/os_venv/bin/python /install_dependencies.py")
echo "Container ID: $CONTAINER_ID"

docker wait "$CONTAINER_ID"

docker logs "$CONTAINER_ID"
# Commit the container to a new image
docker commit "$CONTAINER_ID" app_env:latest

# Remove the container
docker rm "$CONTAINER_ID"

echo "Image built and updated successfully: app_env:latest"
