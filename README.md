# Bot chistes para WhatsApp
Este proyecto sirve para enviar chistes malos a tus amigos de WhatsApp, mediante pyperclip, pyautogui y webbrowser.

## Instalación
Clona el repositorio y entra dentro del directorio.

```bash
git clone https://github.com/cigital/bot-chistes-WhatsApp && cd bot-chistes-WhatsApp
```
Dale permisos de ejecucion al archivos "install.sh".
```bash
chmod +x ./install.sh ./uninstall.sh
```

## Desinstalación

Para desinstalar, ejecuta el archivo "uninstall.sh"

```bash
./uninstall.sh
```

## Como usar
Para usar el programa tienes que reemplazar en el archivo "bot.py" en la linea 18 las x con el numero de tus contactos, si necesitas mas o menos contactos puedes borrar o añadir llaves y valores en el dictionario.

Primero entra en el entorno.
```bash
source entorno/bin/activate
```

Y ejecuta "bot.py" .
```python
python3 bot.py
```

Para salir del entorno simplemente escribe deactivate
```bash
deactivate
```
## Referencias

![Documentación de Pyautogui](https://pyautogui.readthedocs.io/en/latest/)

![Video de donde me inspire](https://youtu.be/gbzNzBUcRzs)
