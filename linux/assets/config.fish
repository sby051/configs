# Environment variables

# fish
set -gx FISH_CONFIG_FILE = "$FISH_CONFIG_DIR/config.fish"
# fish end

# flutter
set -gx FLUTTER_DIR "/opt/flutter/bin"
set -gx PATH "$FLUTTER_DIR" $PATH
# flutter end

# rust / cargo
set -gx CARGO_DIR "/opt/cargo/bin"
set -gx PATH "$CARGO_DIR" $PATH
# rust / cargo end

# cmake
set -gx CMAKE_DIR "/opt/cmake/bin"
set -gx PATH "$CMAKE_DIR" $PATH
# cmake end

# Aliases
alias apt="aptitude"
alias apt-uu="sudo apt update && sudo apt upgrade -y"
alias apt-uuu="sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y && sudo apt autoclean -y"
alias apt-up="sudo apt update"
alias apt-ug="sudo apt upgrade -y"
alias apt-i="sudo apt install"
alias apt-r="sudo apt remove"
alias apt-rr="sudo apt remove --purge"
alias apt-a="sudo apt autoremove -y"
alias apt-c="sudo apt autoclean -y"
alias apt-s="sudo apt search"
alias apt-si="sudo apt show"
alias apt-sii="sudo apt show --installed"
alias cls="clear"
alias l="exa"
alias ls="exa -l --group-directories-first -h -F"
alias root="sudo su"
alias .1="cd .."
alias .2="cd ../.."
alias .3="cd ../../.."
alias .4="cd ../../../.."
alias .5="cd ../../../../.."
alias md="mkdir"
alias edit-alias="nano ~/.config/fish/config.fish"
alias update-alias="source ~/.config/fish/config.fish && cp ~/.config/fish/config.fish ~/repos/configs/linux/assets"
alias python="python3.11"
alias py="python"
alias pip="pip3"
alias nmap!="nmap -v -sC -sV -oN nmap.log $1"
alias cat="batcat"
alias home="cd && clear"
alias gobuster!="gobuster dir -u $1 -w ~/repos/pentesting/tools/wordlists/directory/directory-list.txt -o gobuster.log"

# Startup commands
nvm use latest
clear
