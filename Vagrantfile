# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "rockylinux/9"
  config.vm.synced_folder '.', '/vagrant', type: 'rsync', disabled: false

  config.vm.provider "libvirt" do |libvirt|
    libvirt.cpus = 2
    libvirt.memory = 512
  end

  config.vm.provision "shell", run: "once", inline: <<-SHELL
    dnf update -y --refresh
    dnf install -y make python3-pip
    echo '[[ "`pwd`" == "/home/vagrant" ]] && cd /vagrant' >> /home/vagrant/.bashrc
  SHELL

  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    cd /vagrant
    make setup
  SHELL
end
