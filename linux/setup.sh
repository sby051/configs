#!/bin/bash

echo "Installing initial dependencies..."
sudo apt update -y -qq -o Dpkg::Use-Pty=0
sudo apt upgrade -y -qq -o Dpkg::Use-Pty=0
sudo apt install python3.11 -y -qq -o Dpkg::Use-Pty=0
sudo apt install python3-pip -y -qq -o Dpkg::Use-Pty=0
mkdir -p $HOME/repos
cd $HOME/repos
git clone https://github.com/sby051/configs.git
cd configs/linux
python3.11 main.py
cd
