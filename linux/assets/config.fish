# Start up commands
cd
clear
nvm use node

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
alias update-alias="source ~/.config/fish/config.fish"
alias python="python3.11"
alias py="python"
alias pip="pip3"
alias nmap!="nmap -v -sC -sV -oN nmap.log $1"
alias gobuster!="gobuster dir -u $1 -w ~/repos/pentesting/tools/wordlists/directory/directory-list.txt -o gobuster.log"

# Functions
function fish_prompt -d "Write out the prompt"
    set_color 333942
    echo -n "┌──("
    set_color green
    echo -n $USER
    echo -n "@"
    echo -n $hostname
    set_color 333942
    echo -n ")──["
    set_color blue
    echo -n (prompt_pwd)
    set_color 333942
    echo -n "]"
    set_color yellow
    echo (fish_git_prompt)
    set_color 333942
    echo -n "└─"
    set_color normal
    echo -n "\$ "
end