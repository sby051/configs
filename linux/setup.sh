# Simply installs python3.11 and python3-pip and runs the main.py file
sudo apt update -y 
sudo apt upgrade -y
sudo apt install python3.11 -y
sudo apt install python3-pip -y
git clone https://github.com/sby051/linconf.git
cd linconf
sudo python3.11 main.py
