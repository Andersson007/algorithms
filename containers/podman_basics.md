# Podman basics

## Test yourself

* What is an image
* What is a container

* Get documentation in CLI (2 ways)

* Download an image
* See downloaded images
* Remove an image

* Show running containers
* Show all containers
* Run a container with entrypoint output
* Run a container in detached mode (optionaly with autoremoval option)
* Run in detached mode, specifying name and port
* Set environment variable option
* Stop a container
* Remove a container

* Get logs
* Enter container's shell or execute any other arbitrary command inside

* What is the default network all containers are connected to
* List networks
* Inspect a network, check if DNS is enabled or not
* Create a network
* Create a container attached to the network
* Connect an existing running container to another network
* Inspect container network settings
* Ping one container from inside another container


## Info

```
man podman-<cmd>

podman <cmd> --help
```

## Images

```
$ podman pull <image>

$ podman images

$ podman podman rmi <image>
```

## Containers

```
$ podman ps         # Shows running containers

$ podman ps -a      # Shows all

$ podman run <image>    # Runs not in detached mode, you'll see entrypoint output
```

```
$ podman run -d --name <name> -p <hport>:<cport> <image>
```

Some other useful options:
```
--rm
-e <env-var>
```

```
podman run --rm -e GREET=Hello -e NAME='Red Hat' \
  registry.ocp4.example.com:8443/ubi9/ubi-minimal:9.5
```

```
$ podman exec -it <name|id> sh      # Execute sh interactively inside

$ podman stop <name|id>

$ podman rm <name|id>
```

## Debugging

```
$ podman run <image>        # You'll see entrypoint output

$ podman logs <name|id>     # You'll see whatever logs are available
```

## Networking

```
$ podman network ls

$ podman network inspect <net>

$ podman network create <net-name>

$ podman run -d --name <name> --net <net> -p <HP:CP> <img>

$ podman inspect <container> | jq .[].NetworkSettings.Networks

$ podman network connect <net> <container>

$ podman exec <container> ping <ip|dns>
```
