#!/bin/bash

sudo apt update -y 
sudo apt upgrade -y
sudo apt install python3.11 -y
sudo apt install python3-pip -y
git clone https://github.com/sby051/configs.git ~/repos/configs
cd ~/repos/configs/linux
sudo python3.11 main.py
