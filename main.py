# pip install pynput==1.7.6
from pynput import keyboard
text = ""
other = ""

def pressKey(key):
    global text, other
    if key == keyboard.Key.enter:
        text = "\n"
        other = "\n"
    elif key == keyboard.Key.tab:
        text = "\t"
        other += "\t"
    elif key == keyboard.Key.space:
        text = " "
        other += " "
    elif key == keyboard.Key.shift:
        text = ""
    elif key == keyboard.Key.backspace and len(other) == 0:
        pass
    elif key == keyboard.Key.backspace and len(other) > 0:
        text = "\n" + other[:-1]
        other = other[:-1]
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        text = ""
    else:
        text = str(key).strip("'")
        other += str(key).strip("'")
    print(text, end="")

with keyboard.Listener(
    on_press=pressKey) as listener:
    listener.join()