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
* List port mapping for a container / for all containers
* See how the container was exactly created in CLI

* What are the layers
* How registries and your local system store images
* How to print env vars inside a container
* How to copy a file from your system to a container
* How to copy a file from a container to your system

* How to stop a container when it doesn't respond to podman stop
* How to restart a container with one command

* What you typically have in your Container file
* What is your system-wide container registries conf file

** What is your personal container registries conf file, it's location
** How to get info about the file
** How to see image metadata. What you should look for
** How to copy an image from one registry to another

* How to build a container
* Most basic Containerfile content
* Add a tag (== a new name) to a container
** What is the typical name format
* Push it to a registry
* How to see an image entry point
** How to check pip, rpm, and apt packages installed to an image
* How to save/load image to/from a tar file

* See Containerfile instructions man page
* What do the following instructions do: FROM, RUN, COPY, LABEL,
  VOLUME, ENV, WORKDIR, EXPOSE USER, ENTRYPOINT
* How to install anything using dnf w/o it asking for confirmation
* How to grant non-root filesystem permissions to run files

* skopeo command information (2 ways)
* How to copy files from URLs or unpack tar archives in the destination image in Containerfile
* How to change a working directory during image build
* How to copy everything from the current directory to a current directory inside an image.
  You should change your location inside the image first


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

$ podman port <container>
$ podman port --all

$ podman inspect <container> | less     # Search for CreateCommand
```

## Accessing containers

```
$ podman exec <container> env

$ podman cp <SRC> <DST>     # podman cp local.txt web3:/tmp/local.txt
```

## Managing the container lifecycle

```
$ podman kill <container>  # when it doesn't respond to podman stop

$ podman restart <container>
```

## Container images

```
$ sudo vim /etc/containers/registries.conf

$ mkdir -p ~/.config/containers
$ vim ~/.config/containers/registries.conf

$ man containers-registries.conf

$ podman inspect <registry/repo/image:tag> | less   # Search for "Config"
$ skopeo inspect docker://<registry/repo/image:tag>

# Copy an image from one registry to another
$ skopeo copy --dest-tls-verify=false <SRC> <DST>
```

## Managing Images

```
$ podman build -f Containerfile -t <registry:port/nspace/imgname:tag>

$ podman tag <ID/name> <another-name:tag>

$ podman push <registry:port/nspace/imgname:tag>

$ podman inspect <img>   # To see entry point, look for Config > Cmd

# To see installed packages:
$ podman run --rm <img> python3 -m pip list
$ podman run --rm <img> rpm -qa
$ podman run --rm <img> apt list --installed

# To save/load an image to/from a file
$ podman save -o <file>.tar <img-name>
$ podman load -i <file>.tar
```

The most basic Containerfile
```
FROM <base-image>
CMD <any command>
```

## Custom Container Images

```
# These instructions prepare the container to run Apache HTTP Server
# securely as a non-root user by making specific system directories
# writable by any user belonging to the root group (GID 0).
# 1. chgrp -R: Recursively changes the group ownership of the specified directories and their contents.
# 2. g=u: Copies the owner’s (u-ser) permissions to the g-roup permissions.

RUN dnf install -y httpd && \
    dnf clean all && \
    chgrp -R 0 /var/log/httpd /var/run/httpd && \
    chmod -R g=u /var/log/httpd /var/run/httpd

USER 1001
```
