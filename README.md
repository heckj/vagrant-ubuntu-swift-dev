# vagrant-ubuntu-swift-dev

This is a fork of the IBM-Swift vagrant image for developing
[swift](https://swift.org/). This fork was modified to load a snapshot from
swift.org to more conveniently try server side development with swift. You can
find more on getting started with Swift at
[swift.org/getting-started](https://swift.org/getting-started/)

This repository provides a `Vagrantfile` which will automatically provision and
configure swift with Ubuntu 16.04 as a development environment. It also includes
the tooling to create a Docker based development snapshot

The Vagrantfile will:

1. Install an Ubuntu 16.04 virtual machine
2. Install development prerequisites
3. Install a swift compiler and related tool chain

# Prerequisites
1. [git](https://git-scm.com)
2. [Vagrant](https://www.vagrantup.com)
3. [Virtualbox](https://www.virtualbox.org)

The script `update_swift_snapshot.py` will download the latest development
snapshot and build an Ubuntu 16.04 based docker image with it installed.

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
Swift version 3.1-dev (LLVM cf8fb2a946, Clang fc4e9393a7, Swift 52601c0e98)
Target: x86_64-unknown-linux-gnu
vagrant@vagrant:~$ swift
Welcome to Swift version 3.1-dev (LLVM cf8fb2a946, Clang fc4e9393a7, Swift 52601c0e98). Type :help for assistance.
  1>
```

---

# Docker Usage Guide

```
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
./update_swift_snapshot.py
```

The docker image is built as `swiftpm-docker-1604`:

```
$ docker images
REPOSITORY            TAG                 IMAGE ID            CREATED             SIZE
swiftpm-docker-1604   latest              42a3076b7676        8 minutes ago       1.39 GB
<none>                <none>              5dce2557ba11        18 minutes ago      840 MB
ubuntu                16.04               f49eec89601e        8 days ago          129 MB
```
