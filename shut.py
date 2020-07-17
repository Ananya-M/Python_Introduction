import tkinter as tk
import keyboard, time, os
from functools import partial


def shut(e1):
    mins=float(e1.get())
    secs=mins*60
    time.sleep(secs)
    keyboard.press_and_release('win+d','alt+F4')
    
    #keyboard.press_and_release('alt+F4')
    time.sleep(0.1)
    keyboard.press_and_release('enter')
    

root=tk.Tk()
root.title("Delay")
tk.Label(root, text="Enter time in minutes").grid(row=0)
e1 = tk.Entry(root)
e1.grid(row=0, column=1)
tk.Button(root, text='Run', command=partial(shut,e1)).grid(row=4, column=1,  pady=4)
root.mainloop()
