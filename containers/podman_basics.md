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
* Stop a container
* Remove a container

* Get logs
* Enter container's shell or execute any other arbitrary command inside


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

$ podman exec -it <name|id> sh      # Execute sh interactively inside

$ podman stop <name|id>

$ podman rm <name|id>
```

## Debugging

```

$ podman run <image>        # You'll see entrypoint output

$ podman logs <name|id>     # You'll see whatever logs are available
```
