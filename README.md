# Muvt Mouse
 
## Variabili principali
 
| Variabile | Default | Descrizione |
|---|---|---|
| `IDLE_SECONDS` | `60` | Secondi di inattività prima di muovere il mouse |
| `JIGGLE_PX` | `50` | Pixel di spostamento |
| `in_orario()` | 09:00-13:00 / 14:00-18:00 | Orari in cui il programma è attivo |
 
## Compilare il .exe

Comando di compilazione (da fare dentro la cartella nel cmd):
```
python -m PyInstaller --onefile --windowed --name "Muvt Mouse" --icon=mouse_keeper.ico --hidden-import pynput.mouse --hidden-import pynput.keyboard --hidden-import pystray._win32 mouse_keeper.py
```
 
Il file `.exe` verrà creato nella cartella `dist\`.
 




