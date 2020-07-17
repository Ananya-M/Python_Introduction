import tkinter as tk
import keyboard, time, os
from functools import partial
import os;

def delay():
    branch = tk.Toplevel(root)
    branch.title("Delay")
    tk.Label(branch, text="Enter time in minutes").grid(row=0)
    e1 = tk.Entry(branch)
    e1.grid(row=0, column=1)
    tk.Button(branch, text='Run', command=partial(shut,e1)).grid(row=4, column=1,  pady=4)

def shut(e1):
    mins=float(e1.get())
    secs=mins*60
    time.sleep(secs)
    os.system("shutdown /s /t 1");
    

root=tk.Tk()
root.title("Shut Down?")
tk.Label(root,text="Do you want to shut down this machine?").grid(row=0)
tk.Button(root, text='Yes', command=partial(delay)).grid(row=1, column=0,  pady=4)
tk.Button(root, text='No', command=root.destroy).grid(row=1, column=1,  pady=4)
root.mainloop()
