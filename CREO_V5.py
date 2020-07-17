sml="~ Command `ProCmdModelOpen` \n~ Trail `UI Desktop` `UI Desktop` `DLG_PREVIEW_POST` \ \n `file_open`\n~ Update `file_open` `Inputname` `b.prt`\n~ FocusIn `file_open` `EMBED_BROWSER_SEARCH_IP`\n~ FocusOut `file_open` `EMBED_BROWSER_SEARCH_IP`\n~ Command `ProFileSelPushOpen@context_dlg_open_cmd`\n"
st="!trail file version No. 1600\n!Creo  TM  2.0  (c) 2018 by PTC Inc.  All Rights Reserved.\n"
opc="~ Command `ProCmdModelOpen`\n~ Trail `UI Desktop` `UI Desktop` `DLG_PREVIEW_POST` \\n `file_open`\n~ Update `file_open` `Inputname` `b.prt`\n~ FocusIn `file_open` `EMBED_BROWSER_SEARCH_IP`\n~ FocusOut `file_open` `EMBED_BROWSER_SEARCH_IP`\n~ Command `ProFileSelPushOpen@context_dlg_open_cmd`\n~ Command `ProCmdModelSaveAs`\n~ Open `file_saveas` `type_option`\n~ Close `file_saveas` `type_option`\n~ Select `file_saveas` `type_option` 1 `db_617`\n~ Activate `file_saveas` `Current Dir`\n~ Activate `file_saveas` `OK`\n>M dwg_sel_Alt_key_CB ProeWin3 381 586 100c0 0 1341 0 0 637 1600 0 0 900 13\n~ Select `intf_profile` `pdf_export.pdf_color_depth` 1 `pdf_mono`\n~ Select `intf_profile` `pdf_export.PDFMainTab` 1 `pdf_export.PDFContent`\n~ Select `intf_profile` `pdf_export.pdf_layers_opt` 1 `pdf_layers_all`\n~ Select `intf_profile` `pdf_export.pdf_font_stroke` 1 `pdf_stroke_all`\n~ Activate `intf_profile` `OkPshBtn`\n~ Command `ProCmdWinCloseGroup`\n~ Command `ProCmdModelEraseNotDisp`\n~ Activate `file_erase_nd` `ok_pb`\n"
step="~ Command `ProCmdModelOpen`\n~ Trail `UI Desktop` `UI Desktop` `DLG_PREVIEW_POST` \ \n `file_open`\n~ Update `file_open` `Inputname` `b.prt`\n~ FocusIn `file_open` `EMBED_BROWSER_SEARCH_IP`\n~ FocusOut `file_open` `EMBED_BROWSER_SEARCH_IP`\n~ Command `ProFileSelPushOpen@context_dlg_open_cmd`\n~ Command `ProCmdModelSaveAs` \n~ Open `file_saveas` `type_option`\n~ Close `file_saveas` `type_option`\n~ Select `file_saveas` `type_option` 1 `db_539`\n~ Update `file_saveas` `Inputname` `C:\\Users\\20031748\\Desktop\\TEST WORKING DIRECTORY\\example`\n~ Activate `file_saveas` `OK`\n~ Activate `intf_export` `intf_export`\n~ Activate `intf_export` `OkPushBtn`\n~ Command `ProCmdWinCloseGroup` \n~ Command `ProCmdModelEraseNotDisp` \n~ Activate `file_erase_nd` `ok_pb`\n"
#set working dir string
swd="~ Command `ProCmdSessionChangeDir` \n~ Trail `UI Desktop` `UI Desktop` `DLG_PREVIEW_POST` \\n `file_open`\n~ Activate `file_open` `desktop_pb`\n~ Select `file_open` `Ph_list.Filelist` 1 `SYMBOLS`\n~ Activate `file_open` `Ph_list.Filelist` 1 `SYMBOLS`\n~ FocusOut `file_open` `opt_EMBED_BROWSER_TB_SAB_LAYOUT`\n~ Activate `file_open` `Current Dir`\n~ Update `file_open` `Inputname` `C:\\Users\\20031748\\Desktop\\SYMBOLS\\`\n\n~ Command `ProFileSelPushOpen@context_dlg_open_cmd`"
import os
import tkinter as tk
from functools import partial
import win32gui, keyboard, time
import pyperclip
from tkinter import filedialog

#print(step)

root = tk.Tk()

root.title("Creo GUI")

v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Python

languages = [
    ("PDF"),
    ("DXF"),
    ("Open Files"),
    ("STEP"),
    ("BATCH PURGE"),
    ("HELP")
]

def create_trial_for_PDF(e1,e3):
    b=e1.get()
    print (b)
    path=b.replace("\\","\\\\")
    extn=".drw"
    tf=e3.get()+".txt"
    print(path,extn,tf)
    
    files = []
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
        li.append(opc.replace("b.prt",files[i],1))
        i+=1
    f=open(tf, "w+")
    f.write(st)
        
    for i in li:
        f.write(i)
    f.close()
    global tf_p
    tf_p=os.path.abspath(tf)

#Function to create trail file to open files
def create_trial_to_open(e1,e2,e3):
    b=e1.get()
    print (b)
    path=b.replace("\\","\\\\")
    extn=e2.get()
    tf=e3.get()+".txt"
    print(path,extn,tf)
    
    files = []
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
        i+=1
    f=open(tf, "w+")
    f.write(st)
        
    for i in li:
        f.write(i)
    f.close()
    global tf_p
    tf_p=os.path.abspath(tf)

def create_trial_for_step(e1,e2,e3,e4):
    b=e1.get()
    #print (b)
    path=b.replace("\\","\\\\")
    c=e4.get()
    tpath=c.replace("\\","\\\\")+"\\\\"
    #print(tpath)
    extn="."+e2.get()
    tf=e3.get()+".txt"
    #print(path,extn,tf)
    
    files = []
    filewoexn=[]
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if extn in file:
                #files.append(os.path.join(r, file))
                a=file.split(".")[:-1]
                files.append(a[0]+extn)
                filewoexn.append(a[0])
    

    #for f in files:
        #print(f)
    fc=len(files)
    print(fc)
    i=0
    li=[]
    while (i<fc):
        step1=step.replace("b.prt",files[i])
        step2=step1.replace("C:\\Users\\20031748\\Desktop\\TEST WORKING DIRECTORY\\",tpath)
        li.append(step2.replace("example",filewoexn[i]))
        i+=1
    f=open(tf, "w+")
    f.write(swd.replace("C:\\Users\\20031748\\Desktop\\SYMBOLS\\",path))
    f.write(st)
        
    for i in li:
        f.write(i)
    f.close()
    global tf_p
    tf_p=os.path.abspath(tf)

def create_trial_to_purge(e3):
    master = tk.Toplevel(root) 
    master.title("BATCH PURGE")
    master.grab_set()
    fdc=int(e3.get())
    i=1
    folders=[]
    while (i<=fdc):
        tk.Label(master, text="Folder").grid(row=i)
        e10 = tk.Entry(master)
        e10.grid(row=i, column=1)
        folders.append(e10)
        i+=1
    #print(folders)
    tk.Label(master, text="Trail file name").grid(row=i+1)
    e3 = tk.Entry(master)
    e3.grid(row=i+1, column=1)
    tk.Button(master, text='Close', command=master.destroy).grid(row=i+2, column=0,  pady=4)
    tk.Button(master, text='Run Trail File', command=run_trial).grid(row=i+2, column=1,  pady=4)
    tk.Button(master, text='Create Trail file', command=partial(print_1,folders,e3)).grid(row=i+2, column=2,  pady=4)

    #master.mainloop( )

def print_1(folders,e3):
    l=0
    path=[]
    l1="~ Command `ProCmdSessionChangeDir`\n~ Trail `UI Desktop` `UI Desktop` `DLG_PREVIEW_POST` \\\n`file_open`\n"
    l2="~ Command `ProFileSelPushOpen@context_dlg_open_cmd` \n~ Command `ProCmdWinOpenSystem`\n"
    
    y=[]
    while(l<len(folders)):
        z=folders[l].get()
        y.append(z)
        x=(folders[l].get()).replace("\\","\\\\")
        path.append(x)
        print(path)
        l+=1
    temp=""
    
    tf=e3.get()+".txt"
    f=open(tf, "w+")
    f.write(st)
    l=0
    while(l<len(folders)):
        f.write(l1)
        temp=y[l]
        l4="~ Update `file_open` `Inputname` "+"`"+path[l]+"\\"+"`"+"\n"
        l5="!%CISuccessfully changed to "+y[l]+"\\ directory.\n"
        print(l4,l5)
        f.write(l4)
        f.write(l5)
        f.write(l2)
        l+=1
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
    keyboard.press_and_release('ctrl+v')
    keyboard.press_and_release('enter')
    
def PDF():
    master = tk.Toplevel(root) 
    master.title("PDF")
    master.grab_set()
    tk.Label(master, text="Directory").grid(row=0)
    tk.Label(master, text="Trail file name").grid(row=2)
    e1 = tk.Entry(master)
    e3 = tk.Entry(master)
    e1.grid(row=0, column=1)
    e3.grid(row=2, column=1)
    tk.Button(master, text='Close', command=master.destroy).grid(row=3, column=0,  pady=4)
    tk.Button(master, text='Create Trail to Craete PDFs', command=partial(create_trial_for_PDF,e1,e3)).grid(row=3, column=1,  pady=4)
    tk.Button(master, text='Run', command=run_trial).grid(row=3, column=2,  pady=4)    
    #master.mainloop( )
    
def DXF():
    master = tk.Toplevel(root)
    master.title("DXF")
    master.grab_set()
    msg = tk.Message(master, text ="Coming Soon!")
    msg.config(width=200,font=('times', 24, 'italic'))
    msg.pack()
    tk.Button(master, text='Close', command=master.destroy).pack()
    #master.mainloop()
    
def OPEN_FILES():
    master = tk.Toplevel(root)
    master.title("Open Files")
    master.grab_set()
    tk.Label(master, text="Directory").grid(row=0)
    tk.Label(master, text="Extension").grid(row=1)
    tk.Label(master, text="Trail file name").grid(row=2)
    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e3 = tk.Entry(master)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    tk.Button(master, text='Close', command=master.destroy).grid(row=3, column=0,  pady=4)
    tk.Button(master, text='Create Trail to Open Files', command=partial(create_trial_to_open,e1,e2,e3)).grid(row=3, column=1,  pady=4)
    tk.Button(master, text='Run', command=run_trial).grid(row=3, column=2,  pady=4)    
    #master.mainloop()

def STEP():
    master = tk.Toplevel(root)
    master.title("STEP")
    master.grab_set()
    tk.Label(master, text="Working Directory").grid(row=0)
    tk.Label(master, text="Extension").grid(row=1)
    tk.Label(master, text="Trail file name").grid(row=2)
    tk.Label(master, text="Target Directory").grid(row=3)
    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e3 = tk.Entry(master)
    e4 = tk.Entry(master)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    #tk.Button(master, text='Browse',command=filedialog.askdirectory).grid(row=0, column=2,pady=4)
    #tk.Button(master, text='Browse',command=filedialog.askdirectory).grid(row=3, column=2,pady=4)
    tk.Button(master, text='Close', command=master.destroy).grid(row=4, column=0,  pady=4)
    tk.Button(master, text='Create Trail to Save As STEP', command=partial(create_trial_for_step,e1,e2,e3,e4)).grid(row=4, column=1,  pady=4)
    tk.Button(master, text='Run', command=run_trial).grid(row=4, column=2,  pady=4)    
    #master.mainloop()

def PURGE():
    master = tk.Toplevel(root) 
    master.title("BATCH PURGE")
    master.grab_set()
    tk.Label(master, text="No Of Folders").grid(row=0)
    #tk.Label(master, text="Trail file name").grid(row=2)
    e1 = tk.Entry(master)
    #e3 = tk.Entry(master)
    e1.grid(row=0, column=1)
    #e3.grid(row=2, column=1)
    tk.Button(master, text='Close', command=master.destroy).grid(row=3, column=0,  pady=4)
    tk.Button(master, text='Go', command=partial(create_trial_to_purge,e1)).grid(row=3, column=1,  pady=4)
    #tk.Button(master, text='Run', command=run_trial).grid(row=3, column=2,  pady=4)    
    #master.mainloop( )

def HELP():
    master = tk.Toplevel(root)
    master.title("How to Use this tool")
    master.grab_set()
    msg = tk.Message(master, text ="For updated get in touch with me at nithish.m@ltts.com")
    msg.config(width=200,font=('times', 14, 'italic'))
    msg.pack()
    tk.Button(master, text='Close', command=master.destroy).pack()
    #master.mainloop()    
    
    
    
def ShowChoice():
    if (v.get()==0):
        PDF()
    if(v.get()==1):
        DXF()
    if(v.get()==2):
        OPEN_FILES()
    if(v.get()==3):
        STEP()
    if(v.get()==4):
        PURGE()
    if(v.get()==5):
        HELP()
        
    
        

tk.Label(root, 
         text="Choose the action to be performed",
         justify = tk.LEFT,
         padx = 20).pack()

for val, language in enumerate(languages):
    tk.Radiobutton(root,text=language,padx = 20,variable=v,command=ShowChoice,value=val).pack(anchor=tk.W)
tk.Button(root, text='Close', command=root.destroy).pack()
#tk.Button(root, text='Help', command=HELP).pack()
root.mainloop()
