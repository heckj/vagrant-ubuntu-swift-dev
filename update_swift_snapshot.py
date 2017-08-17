#!/usr/bin/env python

# Dependencies:
# PyYAML
import yaml
import urllib2
import subprocess
import os

url = "https://swift.org/builds/development/ubuntu1604/latest-build.yml"
# Get latest snapshot name.
data = yaml.load(urllib2.urlopen(url).read())
# FIXME: We shouldn't need to do this, it should be available in the API.
latestSnapshot = data["download"].replace("-ubuntu16.04.tar.gz", "")
snapshot = url.rsplit('/', 1)[0] + '/' + latestSnapshot + '/' + data["download"]

print data

if data["download"] in os.listdir("."):
    print("Not downloading: " + snapshot)
else:
    ret = subprocess.call(["wget", snapshot])
    if ret != 0:
        log("Unable to install package: " + path)
        exit(1)
# Call docker build:
# docker build -t swiftpm-docker-1604 --build-arg SNAPSHOT=swift-DEVELOPMENT-SNAPSHOT-2016-11-28-a-ubuntu16.04.tar.gz .
subprocess.call(["docker", "build", "-t", "swiftpm-docker-1604", "--build-arg", "SNAPSHOT=%s" % data["download"], "."])
