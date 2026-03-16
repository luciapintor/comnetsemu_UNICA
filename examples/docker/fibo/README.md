# Docker 
This guide demonstrates the process of building Docker images and initiating containers using those images.

Execute the command below to build a Docker image called ```fibo```, which encompasses all necessary packages to execute the fibo.py script:

```
docker build -t fibo .
```

To start a container utilizing the newly built image, use:
```
docker run fibo
```