sml="~ Command `ProCmdModelOpen` \n~ Trail `UI Desktop` `UI Desktop` `DLG_PREVIEW_POST` \ \n `file_open`\n~ Update `file_open` `Inputname` `b.prt`\n~ FocusIn `file_open` `EMBED_BROWSER_SEARCH_IP`\n~ FocusOut `file_open` `EMBED_BROWSER_SEARCH_IP`\n~ Command `ProFileSelPushOpen@context_dlg_open_cmd`\n"
st="!trail file version No. 1600\n!Creo  TM  2.0  (c) 2018 by PTC Inc.  All Rights Reserved.\n"

print(st,"\n",sml)

import os
import tkinter as tk
from functools import partial

def show_entry_fields():
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
        print(i)
        print(li[i])
        i+=1
    f=open(tf, "w+")
    f.write(st)
        
    for i in li:
        f.write(i)
    f.close()

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
tk.Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1,  pady=4)







master.mainloop( )
