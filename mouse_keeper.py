import time
import threading
import sys

try:
    import pynput.mouse as pmouse
    from pynput.mouse import Controller as MouseController
except ImportError:
    print("ERRORE: pip install pynput")
    sys.exit(1)

try:
    import pystray
    from pystray import MenuItem as item
    from PIL import Image, ImageDraw
except ImportError:
    print("ERRORE: pip install pystray pillow")
    sys.exit(1)

IDLE_SECONDS   = 60
CHECK_INTERVAL = 1
JIGGLE_PX      = 50

_lock           = threading.Lock()
_last_move_time = time.time()
_running        = True

def on_move(x, y):
    global _last_move_time
    with _lock:
        _last_move_time = time.time()

def in_orario():
    ora = time.localtime()
    minuti = ora.tm_hour * 60 + ora.tm_min
    mattina    = (9*60 <= minuti < 13*60)
    pomeriggio = (14*60 <= minuti < 18*60)
    return mattina or pomeriggio

def jiggler_loop():
    global _running, _last_move_time
    mouse = MouseController()
    while _running:
        time.sleep(CHECK_INTERVAL)

        if not in_orario():
            continue

        with _lock:
            idle_for = time.time() - _last_move_time
        if idle_for >= IDLE_SECONDS:
            for _ in range(3):
                mouse.move(JIGGLE_PX, 0)
                time.sleep(0.05)
                mouse.move(-JIGGLE_PX, 0)
                time.sleep(0.05)
            with _lock:
                _last_move_time = time.time()

def create_tray_icon():
    size = 64
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([4, 4, 60, 60], fill=(46, 204, 113, 255), outline=(39, 174, 96, 255))
    cx, cy = size // 2, size // 2
    draw.ellipse([cx-8, cy-8, cx+8, cy+8], fill=(255, 255, 255, 255))
    return img

def on_quit(icon, menu_item):
    global _running
    _running = False
    icon.stop()

def main():
    listener = pmouse.Listener(on_move=on_move)
    listener.daemon = True
    listener.start()

    t = threading.Thread(target=jiggler_loop, daemon=True)
    t.start()

    icon_image = create_tray_icon()
    menu = pystray.Menu(
        item("Muvt Mouse — attivo", lambda i, m: None, enabled=False),
        pystray.Menu.SEPARATOR,
        item("Esci", on_quit),
    )
    tray = pystray.Icon("MouseKeeper", icon_image, "Muvt Mouse", menu)
    tray.run()

if __name__ == "__main__":
    main()
