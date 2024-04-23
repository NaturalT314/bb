#!/bin/bash

IMAGE_NAME="bb"

docker build -t $IMAGE_NAME ./bb/

docker run -d -p 8000:8000 $IMAGE_NAME