# Notes on using the Docker snapshot image

baseline docker CLI options:

- `-i`: interactive
- `-t`: allocate a TTY
- `--rm`: remove the ephemeral container when you're done

example

- checking the version string from swift:
  - `docker run -i -t --rm swiftpm-docker-1610 swift --version`

```
Swift version 4.0-dev (LLVM 13d90f33cc, Clang 9d4bf0beef, Swift b2efaab218)
Target: x86_64-unknown-linux-gnu
```

- dropping into `bash` on the image to poke around
  - `docker run -i -t --rm swiftpm-docker-1610 bash`

`swift` is installed to /usr/bin

- cloning, building, and testing the Kitura project

`docker run -it swiftpm-docker-1610`
 - `cd /root`
 - `git clone https://github.com/IBM-Swift/Kitura`
 - `cd /root/Kitura`
 - `swift test`

Part of Vapor project, a C library with Swift bindings

`docker run -it swiftpm-docker-1610`:
- `cd /root`
- `git clone https://github.com/vapor/clibressl.git`
- `cd clibressl/`
- `swift test`

- cloning, building, and testing Vapor

`docker run -it swiftpm-docker-1610`:
- `cd /root`
- `git clone https://github.com/vapor/vapor.git`
- `cd vapor/`
- `swift test`

- using the local directory as a volume mount

 - `docker run -i -t --rm -v $(pwd):/data:rw swiftpm-docker-1610 bash`
 - variation to build & test swiftpm
  - `docker run -t --rm -v $(pwd):/data:rw -w /data swiftpm-docker-1610 /bin/bash -c "./Utilities/bootstrap && .build/debug/swift-test --parallel"`
