import win32clipboard
import keyboard as kb
from Languages import rus, eng
import time

data = ''

def clipboard_data(data):
    time.sleep(0.2)
    kb.send('ctrl+c')
    time.sleep(0.2)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data


def translation(data):
    data = clipboard_data(data)
    for i in data:
        if i in eng and i not in rus:
            layout = dict(zip(map(ord, eng), rus)) # ENG --> RU
        elif i in rus and i not in eng:
            layout = dict(zip(map(ord, rus), eng)) # RU --> ENG
        return data.translate(layout)


kb.add_hotkey('ctrl+alt', lambda: kb.write(translation(data)))
kb.wait()

