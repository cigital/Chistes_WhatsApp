#!/bin/sh 

echo "Desinstalando requisitos..."

pip uninstall -r ./requirements.txt

sudo apt-get uninstall -q -y scrot python3-tk  python3-dev || sudo pacman -R tk

echo -e "\nBorrando el entorno..."

rm -rf entorno

echo -e "\nDesinstalando virtualenv..."

pip uninstall -q virtualenv

echo -e "\nSe acabo la desinstalación"
