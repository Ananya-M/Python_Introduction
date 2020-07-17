import pyautogui
import os
import tkinter as tk
import win32gui, keyboard, time
import xlwt

def close_pulse():
    os.system("taskkill /f /im  WinFormDemo.exe")

def no_sleep():
    try:
       while True:
           pyautogui.moveTo(100, 100, duration=0.25)
           pyautogui.moveTo(200, 100, duration=0.25)
           pyautogui.moveTo(200, 200, duration=0.25)
           pyautogui.moveTo(100, 200, duration=0.25)
    except:
           pyautogui.press('enter')

def new_excel():
    workbook = xlwt.Workbook()
    workbook.save('my_file.xls')

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,text="CLOSE PULSE POP UP",fg="red",command=close_pulse)
button.pack(side=tk.LEFT)
button = tk.Button(frame,text="DO NOT SLEEP",fg="red",command=no_sleep)
button.pack(side=tk.RIGHT)
button = tk.Button(frame,text="NEW EXCEL",fg="red",command=new_excel)
button.pack(side=tk.RIGHT)

root.mainloop()



