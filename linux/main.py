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
ASSETS_PACKAGES_FILE = f"{ASSETS_DIR}/packages.json"
ASSETS_FISH_CONFIG_FILE = f"{ASSETS_DIR}/config.fish"
LOCAL_FISH_CONFIG_FILE_PATH = f"{HOME_DIR}/.config/fish/config.fish"


def print_title(title, divider="-") -> None:
    print("\n")
    print(f" {title.upper()} ".center(TERMINAL_WIDTH, divider))
    print("\n")

def is_installed(package_name: str) -> bool:
    try:
        return "Status: install ok installed" in check_output(["dpkg", "-s", package_name]).decode("utf-8")
    except:
        return False
    
def clear_screen():
    call(["clear"])

def main():
    
    clear_screen()
        
    print_title(f"linux setup")
    
    try:
        with open(ASSETS_PACKAGES_FILE, "r") as file:
            packages = load(file)
            print(f"+ '{ASSETS_PACKAGES_FILE}' loaded successfully.")
    except FileNotFoundError:
        print(f"! '{ASSETS_PACKAGES_FILE}' could not be found. Maybe reclone the repo?")
        exit(1)
    
    print(f"- Home directory: {HOME_DIR}")
    print(f"- Current user: {CURRENT_USER}")
    
    while True:
        print("\nThis script will install the following:")
        print("\n- Apt packages:", ", ".join(packages["apt"]))
        print("\n- Custom packages:", ", ".join(packages["custom"]))
        print("\n- Fish plugins:", ", ".join(packages["fish"]))
        print("\nIt will also configure fish shell for you (aliases etc)")
        choice = input("\nWould you like to continue? [y/n]: ")
        if choice.lower() == "y":
            break
        print_title("exiting")
        exit(0)
        
    print_title("installing apt packages", divider="=")
    for package in packages["apt"]:
        if is_installed(package):
            print(f"- '{package}' is already installed.")
            continue
        
        print(f"> '{package}' not found, installing...")
        try:
            call(["sudo", "apt", "install", "-y", "-qq", "-o", "Dpkg::Use-Pty=0", package])
            print(f"+ '{package}' installed successfully.")
        except:
            print(f"! '{package}' could not be installed.")
        
    print_title("installing custom packages", divider="=")
    for cmd in packages["custom"]:
        print(f"+ Running {cmd}...")
        system(cmd)
        
    print_title("configuring fish shell", divider="=")
    LOCAL_FISH_BINARY_PATH = check_output(["which", "fish"]).decode("utf-8").strip()
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
    
    for plugin in packages["fish"]:
        call(["fish", "-c", f"fisher install {plugin}"])
    
    print_title("done")
    
if __name__ == '__main__':
    main()