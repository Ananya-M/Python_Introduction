import os
import tkinter as tk
from functools import partial
import win32gui, keyboard, time
import pyperclip
from tkinter import filedialog
#tf_p="Z:\\Nithish\\WORK\\FINAL TIME SAVE\\FILES\\DIM SELECT.txt"
tf_p="DIM SELECT.txt"

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
keyboard.press_and_release('alt+f')
time.sleep(1)
keyboard.press_and_release('m')
time.sleep(1)
keyboard.press_and_release('t')
time.sleep(1)
pyperclip.copy(tf_p)
keyboard.press_and_release('ctrl+v')
keyboard.press_and_release('enter')
time.sleep(2)
keyboard.press_and_release('left')
keyboard.press_and_release('right')
keyboard.press_and_release('right')
keyboard.press_and_release('down')
time.sleep(0.5)
keyboard.press_and_release('alt')
time.sleep(2)
keyboard.press_and_release('D')
time.sleep(0.5)
keyboard.press_and_release('B')
#time.sleep(0.5)
#keyboard.press_and_release('shift+home')
#    keyboard.press_and_release('ctrl+c')
 #   keyboard.press_and_release('win+r')
  #  keyboard.press_and_release('ctrl+v')
#keyboard.press_and_release('alt+tab')
#keyboard.press_and_release('down')
#keyboard.press_and_release('alt+D,b')
#keyboard.press_and_release('shift+home')
#keyboard.press_and_release('ctrl+c')
#keyboard.press_and_release('win+r')
#keyboard.press_and_release('ctrl+v')
#keyboard.press_and_release('alt+tab')

