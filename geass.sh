#!/bin/bash
#um presente de Consani

export GEASS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)"

clear


function cpf() {
    local target=$1
    if [ -z "$target" ]; then
        echo -e "\e[1;31m[!] Error: Provide Geass with CPF.\e[0m"
        return 1
    fi
    
    python "$GEASS_DIR/geasscpf.py" "$target"
}
function cep() {
    local target=$1
    if [ -z "$target" ]; then
        echo -e "\e[1;31m[!] Error: Provide Geass with CEP.\e[0m"
        return 1
    fi

    python "$GEASS_DIR/geasscep.py" "$target"
}
function name() {
    local target=$1
    if [ -z "$target" ]; then
        echo -e "\e[1;31m[!] Error: Provide Geass with name.\e[0m"
        return 1
    fi

    python "$GEASS_DIR/geassname.py" "$target"
}
function plate() {
    local target=$1
    if [ -z "$target" ]; then
        echo -e "\e[1;31m[!] Error: Provide Geass with Plate Number.\e[0m"
        return 1
    fi

    python "$GEASS_DIR/geassplate.py" "$target"
}
function sus() {
    local target=$1
    if [ -z "$target" ]; then
        echo -e "\e[1;31m[!] Error: Provide Geass with CPF.\e[0m"
        return 1
    fi

    python "$GEASS_DIR/geasssus.py" "$target"
}
function title() {
    local target=$1
    if [ -z "$target" ]; then
        echo -e "\e[1;31m[!] Error: Provide Geass with Title.\e[0m"
        return 1
    fi

    python "$GEASS_DIR/geasstitle.py" "$target"
}
function void() {
    local target=$1
    if [ -z "$target" ]; then
        echo -e "\e[1;31m[!] Error: Provide Geass with CPF.\e[0m"
        return 1
    fi

    python "$GEASS_DIR/geassvoid.py" "$target"
}
function mail() {
    local target=$1
    if [ -z "$target" ]; then
        echo -e "\e[1;31m[!] Error: Provide Geass with Mail.\e[0m"
        return 1
    fi

    python "$GEASS_DIR/geassmail.py" "$target"
}
function cnpj() {
    local target=$1
    if [ -z "$target" ]; then
        echo -e "\e[1;31m[!] Error: Provide Geass with CNPJ.\e[0m"
        return 1
    fi

    python "$GEASS_DIR/geasscnpj.py" "$target"
}
function phone() {
    local target=$1
    if [ -z "$target" ]; then
        echo -e "\e[1;31m[!] Error: Provide Geass with Phone.\e[0m"
        return 1
    fi

    python "$GEASS_DIR/geassphone.py" "$target"
}
function geasscore() {
    nano "$GEASS_DIR/geass.sh" && source "$GEASS_DIR/geass.sh"
}

printf '\n\e[1;35m--- GEASS: THE POWER OF THE KING ---\e[0m\n\n'

cat "$GEASS_DIR/geassimg.ans"

printf '\n\e[1;35m--- POWER THAT RETURNS ALL CREATION INTO NOTHINGNESS ---\e[0m\n\n'


printf '%-15s %-50s %s\n' 'TOOL' 'COMMAND' 'INFO'
printf '%-15s %-50s %s\n' '--------' '----------------------------------------------' '--------------------------------'
printf '\e[1;31m%-15s\e[0m %-50s %s\n' 'BRDB' '|cpf|phone|mail|title|cnpj|cep|sus|plate|void|' 'Brazilian Governmental Databases'


printf '\n\e[1;35m--- DO YOU ACCEPT THIS CONTRACT AND ITS CONDITIONS? ---\e[0m\n\n'






export -f geasscore
export -f cpf
export -f phone
export -f mail
export -f title
export -f cnpj
export -f cep
export -f sus
export -f plate
export -f void
export -f name

export PS1="\[\e[1;33m\](GEASS)"
exec bash --norc
