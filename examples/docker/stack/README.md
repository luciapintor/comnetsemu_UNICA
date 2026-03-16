# Docker Swarm (Stack)
***Docker Swarm*** is a powerful clustering and orchestration tool provided by Docker. It allows you to manage and deploy containers across multiple nodes (machines) in a coordinated manner.

***A Docker stack*** is a collection of services that make up an application in a specific environment.

This guide demonstrates usage of `docker swarm` tool for running multi-container applications on Docker defined using the yaml file format. The `my-stack.yaml` file is used to define how one or more services (containers) that make up your application are configured. 


1. Initialize and join a docker swarm:
    ```
    docker swarm init
    ```
2. To show the swarm nodes (members):
    ```
    docker node ls
    ```
3. To deploy a stack to the swarm:
    ```
    docker stack deploy --compose-file my-stack.yaml MyStack    
    ```
4. To show the created stack:
    ```
    docker stack ls
    ```
5. To show the services:
    ```
    docker service ls
    ```
6. To show all conainers created by the stack:
    ```
    docker stack ps MyStack
   ```
7. To remove the stack:
    ```
    docker stack ps MyStack
    ```
8. To leave the swarm:
    ```
    docker swarm leave -f
    ```