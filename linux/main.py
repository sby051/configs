#!/usr/bin/python3.11

from subprocess import call, check_output
from shutil import copyfile, get_terminal_size
from os import getenv, system
from typing import Dict, List
from json import load

HOME_DIR = getenv("HOME")
CURRENT_USER = getenv("USER")
TERMINAL_WIDTH = get_terminal_size().columns
ASSETS_DIR = "./assets"
ASSETS_PACKAGES_FILE = f"{ASSETS_DIR}/PACKAGES.json"
ASSETS_FISH_CONFIG_FILE = f"{ASSETS_DIR}/config.fish"
LOCAL_FISH_CONFIG_FILE_PATH = f"{HOME_DIR}/.config/fish/config.fish"
NEW_USER_NAME = "sby051"

def print_title(title, divider="-") -> None:
    print("\n")
    print(f" {title.upper()} ".center(TERMINAL_WIDTH, divider))
    print("\n")

def is_installed(apt_package_name: str) -> bool:
    try:
        return "Status: install ok installed" in check_output(["dpkg", "-s", apt_package_name]).decode("utf-8")
    except:
        return False
    
def clear_screen():
    call(["clear"])

def main():
    
    clear_screen()
        
    print_title(f"linux setup")
    
    try:
        with open(ASSETS_PACKAGES_FILE, "r") as file:
            PACKAGES = load(file)
            print(f"+ '{ASSETS_PACKAGES_FILE}' loaded successfully.")
    except FileNotFoundError:
        print(f"! '{ASSETS_PACKAGES_FILE}' could not be found. Maybe reclone the repo?")
        exit(1)
    
    print(f"- Home directory: {HOME_DIR}")
    print(f"- Current user: {CURRENT_USER}")
    
    while True:
        print("\nThis script will install the following:")
        print("\n- Apt PACKAGES:", ", ".join(PACKAGES["apt"]))
        print("\n- Custom PACKAGES:", ", ".join(PACKAGES["dpkg"]))
        print("\n- Fish plugins:", ", ".join(PACKAGES["fisher"]))
        print(f"\nIt will configure a new user named {NEW_USER_NAME}, and will configure it to use fish shell.")
        choice = input("\nWould you like to continue? [y/n]: ")
        if choice.lower() == "y":
            break
        print_title("exiting")
        exit(0)
        
            
    print_title("installing apt PACKAGES", divider="=")
    for apt_package in PACKAGES["apt"]:
        if is_installed(apt_package):
            print(f"- '{apt_package}' is already installed.")
            continue
        
        print(f"> '{apt_package}' not found, installing...")
        try:
            call(["sudo", "apt", "install", "-y", "-qq", "-o", "Dpkg::Use-Pty=0", apt_package])
            print(f"+ '{apt_package}' installed successfully.")
        except:
            print(f"! '{apt_package}' could not be installed.")
        
    print_title("installing dpkg PACKAGES", divider="=")
    for dpkg_package in PACKAGES["dpkg"]:
        if is_installed(dpkg_package):
            print(f"- '{dpkg_package}' is already installed.")
            continue
        
        print(f"> '{dpkg_package}' not found, installing...")
        try:
            call(["sudo", "dpkg", "-i", dpkg_package])
            print(f"+ '{dpkg_package}' installed successfully.")
        except:
            print(f"! '{dpkg_package}' could not be installed.")
        
    print_title("configuring user", divider="=")
    LOCAL_FISH_BINARY_PATH = check_output(["which", "fish"]).decode("utf-8").strip()
    
    try:
        print(f"- Creating new user {NEW_USER_NAME}...")
        call(["sudo", "useradd", "-m", "-s", LOCAL_FISH_BINARY_PATH, NEW_USER_NAME])
    except:
        print(f"! New user {NEW_USER_NAME} could not be created.")

    try:
        print(f"- Changing default shell to {LOCAL_FISH_BINARY_PATH}...")
        call(["sudo", "chsh", "-s", LOCAL_FISH_BINARY_PATH, CURRENT_USER])
        print(f"+ Default shell changed to {LOCAL_FISH_BINARY_PATH}")
    except:
        print(f"! Default shell could not be changed to {LOCAL_FISH_BINARY_PATH}")
    
    try:
        print("- Copying fish_config...")
        copyfile(ASSETS_FISH_CONFIG_FILE, LOCAL_FISH_CONFIG_FILE_PATH)
        print(f"+ {ASSETS_FISH_CONFIG_FILE} copied to {LOCAL_FISH_CONFIG_FILE_PATH}")
    except:
        print(f"! {ASSETS_FISH_CONFIG_FILE} could not be copied to {LOCAL_FISH_CONFIG_FILE_PATH}")
    
    try:
        print("- Sourcing fish_config...")
        call(["source", LOCAL_FISH_CONFIG_FILE_PATH])
        print(f"+ {LOCAL_FISH_CONFIG_FILE_PATH} sourced successfully.")
    except:
        print(f"! {LOCAL_FISH_CONFIG_FILE_PATH} could not be sourced.")
    
    
    print("- Installing fisher...")
    system("curl -sL https://git.io/fisher | source && fisher install jorgebucaran/fisher")
    print_title("installing fisher plugins", divider="=")
    for plugin in PACKAGES["fisher"]:
        call(["fish", "-c", f"fisher install {plugin}"])
    
    print_title("done")
    
if __name__ == '__main__':
    main()