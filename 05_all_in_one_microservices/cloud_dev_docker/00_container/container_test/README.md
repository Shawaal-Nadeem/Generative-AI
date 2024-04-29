Firstly open Docker Desktop and run engine then go to following commands

## Command to build image: 
        D:\Generative-AI\05_all_in_one_microservices\cloud_dev_docker\00_container>docker build  -f Dockerfile -t container-class .

## Command to see images:
        D:\Generative-AI\05_all_in_one_microservices\cloud_dev_docker\00_container\container_test>docker images

## Command to run container:
        D:\Generative-AI\05_all_in_one_microservices\cloud_dev_docker\00_container\container_test>docker run -d --name testcontainer -p 8000:8000 container-class