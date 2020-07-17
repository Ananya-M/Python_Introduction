sml="~ Command `ProCmdModelOpen` \n~ Trail `UI Desktop` `UI Desktop` `DLG_PREVIEW_POST` \ \n `file_open`\n~ Update `file_open` `Inputname` `b.prt`\n~ FocusIn `file_open` `EMBED_BROWSER_SEARCH_IP`\n~ FocusOut `file_open` `EMBED_BROWSER_SEARCH_IP`\n~ Command `ProFileSelPushOpen@context_dlg_open_cmd`\n"
st="!trail file version No. 1600\n!Creo  TM  2.0  (c) 2018 by PTC Inc.  All Rights Reserved.\n"

print(st,"\n",sml)

import os
import tkinter as tk
from functools import partial
import win32gui, keyboard, time
import pyperclip

def create_trial():
    b=e1.get()
    print (b)
    path=b.replace("\\","\\\\")
    extn=e2.get()
    tf=e3.get()+".txt"
    print(path,extn,tf)
    
    #path = 'Z:\\Nithish\\WORK\\FINAL TIME SAVE'
    files = []
    #files= [".".join(f.split(".")[:-1]) for f in os.listdir() if os.path.isfile(f)]
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if extn in file:
                #files.append(os.path.join(r, file))
                a=file.split(".")[:-1]
                files.append(a[0]+extn)

    #for f in files:
        #print(f)
    fc=len(files)
    print(fc)
    i=0
    li=[]
    while (i<fc):
        li.append(sml.replace("b.prt",files[i],1))
        #print(i)
        #print(li[i])
        i+=1
    f=open(tf, "w+")
    f.write(st)
        
    for i in li:
        f.write(i)
    f.close()
    global tf_p
    tf_p=os.path.abspath(tf)

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
 
def run_trial():
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
    keyboard.press_and_release('m')
    keyboard.press_and_release('t')
    pyperclip.copy(tf_p)
    print(tf_p)
    keyboard.press_and_release('ctrl+v')
    keyboard.press_and_release('enter')


master = tk.Tk()
tk.Label(master, text="Directory").grid(row=0)
tk.Label(master, text="Extension").grid(row=1)
tk.Label(master, text="Trail file name").grid(row=2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
tk.Button(master, text='Quit', command=master.destroy).grid(row=3, column=0,  pady=4)
tk.Button(master, text='Create', command=create_trial).grid(row=3, column=1,  pady=4)
tk.Button(master, text='Run', command=run_trial).grid(row=3, column=2,  pady=4)









master.mainloop( )
