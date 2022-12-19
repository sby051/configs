#!/bin/bash
echo "Installing initial dependencies..."

# update and upgrade the system
sudo apt update -y -qq
sudo apt upgrade -y -qq

# remove any existing python installs
sudo apt remove python3.* -y -qq
sudo apt remove python3-pip -y -qq

# install python 3.11
sudo apt install software-properties-common -y -qq
sudo add-apt-repository ppa:deadsnakes/ppa -y -qq
sudo apt update -y -qq
sudo apt install python3.11 -y -qq

# create a symlink for python3, python and pip3
sudo ln -s $(which python3.11) /usr/bin/python3
sudo ln -s $(which python3.11) /usr/bin/python
sudo ln -s $(which pip3) /usr/local/bin/pip

# install curl and git
sudo apt install curl -y -qq
sudo apt install git -y -qq

# prepare the system for the installation of the configs
mkdir -p $HOME/repos
cd $HOME/repos
git clone https://github.com/sby051/configs.git
cd configs/linux

# install the configs
python main.py
