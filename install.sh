#!/bin/sh 

echo "Instalando virtualenv..."

pip install -q virtualenv

echo -e "\nCreando el directorio..."

mkdir entorno

echo -e "\nCreando el entorno..."

python3 -m virtualenv entorno -q
source entorno/bin/activate 

echo -e "\nInstalando requisitos.."

pip install -r ./requirements.txt -q 

sudo apt-get install -q -y scrot python3-tk  python3-dev || sudo pacman -S tk

echo -e "\nSe acabo la instalación"

