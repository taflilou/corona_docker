# -*- mode: ruby -*-
# vi: set ft=ruby :

# Description: Vagrantfile to create 1 CentOS VM for RHCSA

IP_ADDRESS = '192.168.20.203'

# Looping for each VM
Vagrant.configure("2") do |config|

 # +-----------------+
 # | CentOS RHCSA VM |
 # +-----------------+
 config.vm.define "rhcsa8vm" do |rhcsa8vm|
  rhcsa8vm.vm.box = "generic/centos8"
  rhcsa8vm.vm.hostname = "rhcsa8vm"
  # Sync coronawebapp directory to /vagrant on vm
  rhcsa8vm.vm.synced_folder "mytools", "/vagrant"
  # Specify the network interface specifications
  rhcsa8vm.vm.network "private_network", ip: "#{IP_ADDRESS}"
  # Specify name, memory and gui for VM
  rhcsa8vm.vm.provider "virtualbox" do |vb|
    vb.name = "rhcsa8vm"
    vb.gui = true
    vb.memory = 4096
  # To speed up Vagrant VM
	vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
	vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
    # Add 2 vCPU
    vb.customize ["modifyvm", :id, "--ioapic", "on"]
    vb.customize ["modifyvm", :id, "--cpus", "4"]   
  end

  # Provisionning shell and ansible for the VM
  rhcsa8vm.vm.provision "shell", inline: <<-SHELL
     sudo su
     yum -y install epel-release yum-utils
     yum -y update && yum -y upgrade
     yum -y install gcc vim git ansible python python34-setuptools python34-pip-8.1.2-5.el7.noarch jq mlocate nc net-tools
     yum -y install python-pip python3-pip
     pip install --upgrade pip
     pip install pipenv
     pip3 install pipenv
     updatedb
   SHELL

 end

end
