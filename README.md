# vagrant-ubuntu-swift-dev

This is a fork of the IBM-Swift vagrant image for developing
[swift](https://swift.org/). This fork was modified to load a snapshot from
swift.org to more conveniently try server side development with swift. You can
find more on getting started with Swift at
[swift.org/getting-started](https://swift.org/getting-started/)

This repository provides a `Vagrantfile` which will automatically provision and
configure swift with Ubuntu 16.10 as a development environment. It also includes
the tooling to create a Docker based development snapshot

The Vagrantfile will:

1. Install an Ubuntu 16.10 virtual machine
2. Install development prerequisites
3. Install a swift compiler and related tool chain

# Prerequisites
1. [git](https://git-scm.com)
2. [Vagrant](https://www.vagrantup.com)
3. [Virtualbox](https://www.virtualbox.org)

The script `update_swift_snapshot.py` will download the latest development
snapshot and build an Ubuntu 16.10 based docker image with it installed.

# Prerequisites
1. [git](https://git-scm.com)
2. [Docker](https://www.docker.com/products/overview)

# Vagrant Usage Guide

```
$ git clone https://github.com/heckj/vagrant-ubuntu-swift-dev.git
$ cd vagrant-ubuntu-swift-dev
$ vagrant up
```

Once your VM has been provisioned, connect to it using the `vagrant ssh` command.

`vagrant ssh`:

```
vagrant@vagrant:~$ swift --version
Swift version 4.0-dev (LLVM 13d90f33cc, Clang 9d4bf0beef, Swift b2efaab218)
Target: x86_64-unknown-linux-gnu

vagrant@vagrant:~$ swift
***  You are running Swift's integrated REPL,  ***
***  intended for compiler and stdlib          ***
***  development and testing purposes only.    ***
***  The full REPL is built as part of LLDB.   ***
***  Type ':help' for assistance.              ***
(swift)
```

---

# Docker Usage Guide

```
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
./update_swift_snapshot.py
```

The docker image is built as `swiftpm-docker-1610`:

```
$ docker images
REPOSITORY            TAG                 IMAGE ID            CREATED             SIZE
swiftpm-docker-1610   latest              dce3b5086cbd        15 minutes ago      1.41GB
ubuntu                16.10               7d3f705d307c        3 weeks ago         107MB
```

For more notes on using the docker image locally, see [docker development notes](./docker_devnotes.md)
