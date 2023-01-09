#!/bin/bash
echo "Installing initial dependencies..."

# update and upgrade the system
sudo apt update -y -qq
sudo apt upgrade -y -qq

# install python3
echo "Installing python3..."
sudo apt install python3 -y -qq
sudo apt install python3-pip -y -qq

# install curl and git
echo "Installing curl and git..."
sudo apt install curl -y -qq
sudo apt install git -y -qq

# prepare the system for the installation of the configs
echo "Preparing the system for the installation of the configs..."
mkdir -p $HOME/repos
cd $HOME/repos
git clone https://github.com/sby051/configs.git
cd configs/linux

# install the configs
echo "Installing the configs..."
python3 main.py
