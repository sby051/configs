# environment variables

# lazygit
set -gx LAZYGIT_VERSION (curl -s "https://api.github.com/repos/jesseduffield/lazygit/releases/latest" | grep '"tag_name":' |  sed -E 's/.*"v*([^"]+)".*/\1/')
# lazygit end

# fish
set -gx FISH_CONFIG_FILE "/root/.config/fish/config.fish"
# fish end

# rust / cargo
set -gx CARGO_DIR "/opt/cargo/bin"
set -gx CARGO_HOME_DIR "/root/.cargo/bin"
set -gx PATH "$CARGO_DIR" $PATH
set -gx PATH "$CARGO_HOME_DIR" $PATH
# rust / cargo end

# cmake
set -gx CMAKE_DIR "/opt/cmake/bin"
set -gx PATH "$CMAKE_DIR" $PATH
# cmake end

# aliases
alias lg "lazygit"
alias apt "aptitude"
alias apt-uu "sudo apt update && sudo apt upgrade -y"
alias apt-uuu "sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y && sudo apt autoclean -y"
alias apt-up "sudo apt update"
alias apt-ug "sudo apt upgrade -y"
alias apt-i "sudo apt install"
alias apt-r "sudo apt remove"
alias apt-rr "sudo apt remove --purge"
alias apt-a "sudo apt autoremove -y"
alias apt-c "sudo apt autoclean -y"
alias apt-s "sudo apt search"
alias apt-si "sudo apt show"
alias apt-sii "sudo apt show --installed"

alias cls "clear"
alias sysinfo "screenfetch"
alias l "exa"
alias ls "l -l --group-directories-first -h -F"

alias root "sudo su"
alias .1 "cd .."
alias .2 "cd ../.."
alias .3 "cd ../../.."
alias .4 "cd ../../../.."

alias .5 "cd ../../../../.."

alias md "mkdir"
alias edit-alias "nano $FISH_CONFIG_FILE"
alias update-alias "source $FISH_CONFIG_FILE && cp $FISH_CONFIG_FILE ~/repos/configs/linux/assets"

alias add-alias "echo $1 >> $FISH_CONFIG_FILE && update-alias"
alias python "python3"
alias py "python"

alias pip "pip3"
alias rustscan! "rustscan -a $argv --ulimit=5000 --scan-order "Random" --range 1-10000 -- -A -sC -sV -oN ./rustscan.log"
alias ips "ip addr show eth0 | grep inet | awk '{ print $2; }' | sed 's/\/.*\$//'"
alias nmap! "nmap -v -sC -sV -oN nmap.log $1"
alias cat "batcat"
alias home "cd && clear"
alias gobuster! "gobuster -w /opt/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -x "php,html,css,pdf,txt,js" -o ./gobuster.log -u"
alias untar "tar xf"

# startup commands
nvm use latest

