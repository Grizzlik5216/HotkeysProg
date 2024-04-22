import os
import shutil
import time
import win32clipboard
import keyboard as kb
import glob
from Extensions import extensions

while True:
    kb.wait('ctrl+j')
    if kb.is_pressed('ctrl+j') == True:

        path = ''

        time.sleep(0.2)
        kb.send('ctrl+c')
        time.sleep(0.2)
        win32clipboard.OpenClipboard()
        path = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()

        files = os.listdir(path)

        for extension, folder_name in extensions.items():
            files = glob.glob(os.path.join(path, f"*.{extension}"))
            print(f"[*] Найдено {len(files)} файлов с расширением {extension}.")
            if not os.path.isdir(os.path.join(path, folder_name)) and files:
                os.mkdir(os.path.join(path, folder_name))
                print(f"[+] Создана папка {folder_name}.")

            for file in files:
                basename = os.path.basename(file)
                dst = os.path.join(path, folder_name, basename)
                print(f"[*] Перенесен файл '{file}' в {dst}.")
                shutil.move(file, dst)
