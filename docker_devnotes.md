# Notes on using the Docker snapshot image

baseline docker CLI options:

- `-i`: interactive
- `-t`: allocate a TTY
- `--rm`: remove the ephemeral container when you're done

example

- checking the version string from swift:
  - `docker run -i -t --rm swiftpm-docker-1604 swift --version`

```
Swift version 3.1-dev (LLVM 03606c6a3f, Clang f4873e0e90, Swift 74dcb489e6)
Target: x86_64-unknown-linux-gnu
```

- dropping into `bash` on the image to poke around
  - `docker run -i -t --rm swiftpm-docker-1604 bash`

`swift` installed to /usr/bin, along with the various command aliases:
- `swift-build`
- `swift-package`
- `swift-test`

- cloning, building, and testing the kitura project

`docker run -it swiftpm-docker-1604`
 - `cd /root`
 - `git clone https://github.com/IBM-Swift/Kitura`
 - `cd /root/Kitura`
 - `swift test`

 failures:
  - missing `openssl libssl-dev` dependency from Kitura -> OpenSSL
  - IBM-Swift/SwiftyJSON doesn't appear to be source compatible with Swift 3.1-dev
    - SwiftyJSON/SwiftyJSON doesn't appear to build with this right now either...

- cloning, building, and testing the clibressl project

Part of Vapor project, a C library with Swift bindings

`docker run -it swiftpm-docker-1604`:
- `cd /root`
- `git clone https://github.com/vapor/clibressl.git`
- `cd clibressl/`
- `swift test`

- cloning, building, and testing Vapor

`docker run -it swiftpm-docker-1604`:
- `cd /root`
- `git clone https://github.com/vapor/vapor.git`
- `cd vapor/`
- `swift test`

- using the local directory as a volume mount

 - `docker run -i -t --rm -v $(pwd):/data:rw swiftpm-docker-1604 bash`
 - variation to build & test swiftpm
  - `docker run -t --rm -v $(pwd):/data:rw -w /data swiftpm-docker-1604 /bin/bash -c "./Utilities/bootstrap && .build/debug/swift-test --parallel"`
