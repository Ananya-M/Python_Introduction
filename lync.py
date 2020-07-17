import os
import tkinter as tk
from functools import partial
import win32gui, keyboard, time
import pyperclip
from tkinter import filedialog



def find(e1):
    keyboard.press_and_release('esc') 
    def windowEnumerationHandler(hwnd, top_windows):
        top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
    keyboard.press_and_release('esc') 
    if __name__ == "__main__":
        results = []
        top_windows = []
        win32gui.EnumWindows(windowEnumerationHandler, top_windows)
        for i in top_windows:
            if "skype" in i[1].lower():
                print (i)
                win32gui.ShowWindow(i[0],5)
                win32gui.SetForegroundWindow(i[0])
                break
    name=e1.get()
    keyboard.press_and_release('ctrl+5')
    keyboard.press_and_release('ctrl+1')
    keyboard.write(name)
    time.sleep(0.1)
    keyboard.press_and_release('tab,tab,tab')
    time.sleep(0.1)

    keyboard.press_and_release('apps')
    time.sleep(0.1)
    keyboard.press_and_release('up arrow')
    time.sleep(0.1)
    keyboard.press_and_release('enter')
    time.sleep(0.1)
    keyboard.press_and_release('tab')
    time.sleep(0.1)
    keyboard.press_and_release('tab')
    time.sleep(0.1)
    keyboard.press_and_release('tab')
    time.sleep(0.1)
    keyboard.press_and_release('ctrl+a,ctrl+c')
    #keyboard.press_and_release('tab,tab,tab,tab,tab,ctrl+a,ctrl+c')
    
    status=pyperclip.paste()
    print(status)

  


root = tk.Tk()
root.title("aaa")
tk.Label(root, text="Name").grid(row=0)
e1 = tk.Entry(root)
e1.grid(row=0, column=1)
tk.Button(root, text='Close', command=root.destroy).grid(row=3, column=0,  pady=4)
tk.Button(root, text='Find', command=partial(find,e1)).grid(row=3, column=1,  pady=4)
root.mainloop()

