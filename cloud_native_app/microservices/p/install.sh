#! /bin/bash
sudo apt-get update
sudo apt install -y docker.io

sudo apt-get install -y docker-engine
sudo service docker start
sudo docker build -t microservice_p .
sudo docker run --rm -it -p 8094:8094 microservice_p
