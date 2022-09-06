# Script chistes para WhatsApp
Este script sirve para enviar chistes malos a tus amigos de WhatsApp, mediante pyperclip, pyautogui y webbrowser.

!! ADVERTENCIA, este script solo esta probado en arch linux !!

## Instalación
Clona el repositorio y entra dentro del directorio.

```bash
git clone https://github.com/cigital/bot-chistes-WhatsApp && cd bot-chistes-WhatsApp
```
Dale permisos de ejecucion al archivos "install.sh".
```bash
chmod +x ./install.sh ./uninstall.sh
```

Ejecuta el archivo de instalación.
```bash
./install.sh
```

## Desinstalación
Para desinstalar, ejecuta el archivo "uninstall.sh"
```bash
./uninstall.sh
```

## Como usar
Para usar el script primero tienes que reemplazar en el archivo "bot.py" en la linea 18 las x con el numero de tus contactos.

Despues entra en el entorno.
```bash
source entorno/bin/activate
```

Y ejecuta "bot.py" .
```python
python3 bot.py
```

Para salir del entorno simplemente escribe
```bash
deactivate
```
## Referencias

![Documentación de Pyautogui](https://pyautogui.readthedocs.io/en/latest/)

![Video de donde me inspire](https://youtu.be/gbzNzBUcRzs)
