#!/bin/bash

echo "Installing initial dependencies..."
sudo apt update -y -qq
sudo apt upgrade -y -qq
sudo apt install python3.11 -y -qq
sudo apt install python3-pip -y -qq
mkdir -p $HOME/repos
cd $HOME/repos
git clone https://github.com/sby051/configs.git
cd configs/linux
python3.11 main.py
cd
