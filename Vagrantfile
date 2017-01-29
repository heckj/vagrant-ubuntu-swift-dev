# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  # Swift development targets Ubuntu 16.04
  config.vm.box = "bento/ubuntu-16.04"
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
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -y python-dev
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -y libblocksruntime-dev

    echo "retrieving Swift GPG signing keys"
    wget -q -O - https://swift.org/keys/all-keys.asc | gpg --import -
    gpg --keyserver hkp://pool.sks-keyservers.net --refresh-keys Swift

    echo "installing swift"
    sudo mkdir -p /opt
    cd /opt
    wget -q https://swift.org/builds/swift-3.1-branch/ubuntu1604/swift-3.1-DEVELOPMENT-SNAPSHOT-2017-01-22-a/swift-3.1-DEVELOPMENT-SNAPSHOT-2017-01-22-a-ubuntu16.04.tar.gz
    wget -q https://swift.org/builds/swift-3.1-branch/ubuntu1604/swift-3.1-DEVELOPMENT-SNAPSHOT-2017-01-22-a/swift-3.1-DEVELOPMENT-SNAPSHOT-2017-01-22-a-ubuntu16.04.tar.gz.sig
    gpg --verify swift-*.tar.gz.sig
    tar xzf /opt/swift*.tar.gz
    sudo chown -R vagrant:vagrant /opt
    rm -f swift-*.tar.gz*
    echo "export PATH=/opt/swift-3.1-DEVELOPMENT-SNAPSHOT-2017-01-22-a-ubuntu16.04/usr/bin:\${PATH}" >> ~vagrant/.bashrc
  SHELL
end
