import os, mouse as mo
import tkinter as tk
from functools import partial
import win32gui, keyboard as kb, time
import pyperclip
from tkinter import filedialog
path="\\\\vssstorage\\UTCMechanical\\Nithish\\New Microsoft PowerPoint Presentation.pptm"

kb.press_and_release('win+d')
time.sleep(0.2)
def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
 

if __name__ == "__main__":
    results = []
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    for i in top_windows:
        if "creo parametric" in i[1].lower():
            print (i)
            win32gui.ShowWindow(i[0],5)
            win32gui.SetForegroundWindow(i[0])
            break
kb.press_and_release('alt+space,x')
time.sleep(1)
kb.press_and_release('win+PrtScn')

kb.press_and_release('win+r')
time.sleep(.1)
kb.write(path)
kb.press_and_release('enter')
time.sleep(5)
kb.press_and_release('end')
kb.press_and_release('alt+H,y')
kb.press_and_release('ctrl+v')
kb.press_and_release('ctrl+s')
