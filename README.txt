# Mouse Keeper — Windows

Se il mouse è fermo per 1 minuto esatto, lo muove leggermente (tremolio).
Appena il mouse si muove, il timer si azzera.
Gira silenzioso nel system tray (icona verde vicino all'orologio).

---

## Avvio rapido (richiede Python installato)

1. Doppio click su `install_e_avvia.bat`
2. L'icona verde appare nel tray in basso a destra
3. Per uscire: click destro sull'icona → Esci

---

## Creare un .exe standalone (non richiede Python sul PC)

1. Doppio click su `build_exe.bat`
2. Aspetta ~1 minuto
3. Trovi `mouse_keeper.exe` nella cartella `dist\`
4. Quel file funziona su qualsiasi PC Windows senza installare nulla

---

## Parametri modificabili in mouse_keeper.py

| Costante       | Default | Significato                          |
|----------------|---------|--------------------------------------|
| IDLE_SECONDS   | 60      | Secondi di inattività (1 minuto)     |
| JIGGLE_PX      | 50      | Pixel di spostamento per il tremolio |
