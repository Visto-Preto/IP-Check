#!/data/data/com.termux/files/usr/bin/env bash

echo -e '\n\n'
echo -e '\033[1;31mInstalando dependências...\033[m'
echo -e '\n'
apt update && apt upgrade -y
apt install -y git python figlet cowsay

pip install requests

clear
cowsay Ip-Check
echo -e '\n\n'
echo -e '\033[1;31mInstalando o Ip-Check...\033[m'
echo -e '\n'

git clone https://github.com/Visto-Preto/Ip-Check ipcheck

cat ipcheck/ipcheck.sh > /data/data/com.termux/files/usr/bin/ipcheck
chmod 700 /data/data/com.termux/files/usr/bin/ipcheck
cp -R ipcheck /data/data/com.termux/files/usr/share/
rm -Rf ipcheck

echo -e '\n\n'
echo -e 'Para iniciar o Ip-Check entre com o comando: \033[1;32mipcheck\033[m'
echo -e '\n\n\n'
