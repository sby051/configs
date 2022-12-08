import subprocess 

def main():
    system("clear")
    print("Welcome to the personal setup script!")
    
    try:
        with open("./apt-packages.txt", "r") as file:
            apt_packages = file.readlines()
    except FileNotFoundError:
        print("apt-packages.txt not found, please reclone the repo")
        exit(1)
        
    try:
        with open("./custom-packages.txt", "r") as file:
            custom_packages = file.readlines()
    except FileNotFoundError:
        print("custom-packages.txt not found, please reclone the repo")
        exit(1)
        
    print("Installing apt packages...")
    for package in apt_packages:
        print(f"- Installing {package}...")
        subprocess.call(["sudo", "apt", "install", package, "-y"])
        
    print("Installing custom packages...")
    for package in custom_packages:
        print(f"- Installing {package}...")
        subprocess.call(["sudo", "dpkg", "-i", package])
        
    print("Changing shell to fish...")
    system("chsh -s /usr/bin/fish")
    
    print("Installing fisher & bass...")
    system("curl -sL https://git.io/fisher | source && fisher install jorgebucaran/fisher && fisher install edc/bass")

    print("Configuring fish...")
    system("cp ./config.fish /home/personal/.config/fish/config.fish")    
    
    print("Done!")
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
    # write a curl command to clone the repo and run setup.sh
    curl = "curl -sL https://raw.githubusercontent.com/sby051/linconf/main/setup.sh | bash"
