# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  # Swift development targets Ubuntu 16.04
  config.vm.box = "bento/ubuntu-16.10"
  config.vm.define "swift-dev" do |swiftdev|
  end

  config.vm.provider "virtualbox" do |vb|
    vb.name = "swift-dev"
    # Building swift requires significant resources
    # original was 6GB RAM & 4 cores, trimmed down for my laptop
    vb.memory = "2048"
    vb.cpus = 2
  end

  # Prevents "stdin: is not a tty" on Ubuntu (https://github.com/mitchellh/vagrant/issues/1673)
  config.vm.provision "fix-no-tty", type: "shell" do |s|
    s.privileged = false
    s.inline = "sudo sed -i '/tty/!s/mesg n/tty -s \\&\\& mesg n/' /root/.profile"
  end

  # Initialise development environment
  config.vm.provision "shell", inline: <<-SHELL
    echo "Updating virtual machine..."
    sudo DEBIAN_FRONTEND=noninteractive apt-get update
    sudo DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y

    echo "Installing swift prerequisites..."
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -y git
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -y clang
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -y libicu-dev
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -y libblocksruntime-dev
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -y curl wget rsync
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -y libedit-dev
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -y python2.7 python2.7-dev
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -y python-dev
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -y libcurl4 libcurl4-openssl-dev
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -y libssl-dev openssl
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -y libkqueue-dev

    echo "retrieving Swift GPG signing keys"
    wget -q -O - https://swift.org/keys/all-keys.asc | gpg --import -
    gpg --keyserver hkp://pool.sks-keyservers.net --refresh-keys Swift

    echo "installing swift"
    sudo mkdir -p /opt
    cd /opt
    wget -q https://swift.org/builds/development/ubuntu1610/swift-DEVELOPMENT-SNAPSHOT-2017-08-15-a/swift-DEVELOPMENT-SNAPSHOT-2017-08-15-a-ubuntu16.10.tar.gz
    wget -q https://swift.org/builds/development/ubuntu1610/swift-DEVELOPMENT-SNAPSHOT-2017-08-15-a/swift-DEVELOPMENT-SNAPSHOT-2017-08-15-a-ubuntu16.10.tar.gz.sig
    gpg --verify swift-*.tar.gz.sig
    tar xzf /opt/swift*.tar.gz
    sudo chown -R vagrant:vagrant /opt
    rm -f swift-*.tar.gz*
    echo "export PATH=/opt/swift-DEVELOPMENT-SNAPSHOT-2017-08-15-a-ubuntu16.10/usr/bin:\${PATH}" >> ~vagrant/.bashrc
  SHELL
end
