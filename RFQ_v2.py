import openpyxl as xl
import win32gui, os, time
import keyboard as ky
import pyperclip
import tkinter as tk
from functools import partial
from pptx import Presentation



root=tk.Tk()
root.title("Create RFQ Mail")

sln=[]
part=[]
desc=[]
qty=[]
bd="Hello,\nPlease send us a quote for the below parts.\n"


def mail(i):
    master=tk.Toplevel(root)
    tk.Label(master,text="To:").grid(row=0,column=0)
    tk.Label(master,text="Cc:").grid(row=1,column=0)
    tk.Label(master,text="Subjet:").grid(row=2,column=0)
    e98=tk.Entry(master)
    e98.grid(row=0,column=1)
    e99=tk.Entry(master)
    e99.grid(row=1,column=1)
    e100=tk.Entry(master)
    e100.grid(row=2,column=1)
    tk.Button(master,text='Next',command=partial(outlook,e98,e99,e100,i)).grid(row=i+1,column=0)
    tk.Button(master,text='Close',command=master.destroy).grid(row=i+1,column=1)
    
def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def outlook(e98,e99,e100,i):
    to=e98.get()
    cc=e99.get()
    sub=e100.get()
    if __name__ == "__main__":
        results = []
        top_windows = []
        win32gui.EnumWindows(windowEnumerationHandler, top_windows)
        for j in top_windows:
            if "outlook" in j[1].lower():
                
                win32gui.ShowWindow(j[0],5)
                win32gui.SetForegroundWindow(j[0])
                break
    time.sleep(1)
    ky.press_and_release('ctrl+n')
    ky.press_and_release('alt+space')
    ky.press_and_release('x')
    ky.press_and_release('alt+.')
    ky.press_and_release('tab')
    ky.press_and_release('tab')
    ky.press_and_release('tab')
    ky.press_and_release('tab')
    ky.press_and_release('tab')
    ky.write(to)
    #ky.write("nithish.m@ltts.com")
    ky.press_and_release('tab')
    ky.press_and_release('tab')
    ky.press_and_release('tab')
    ky.press_and_release('enter')
    ky.press_and_release('alt+c')
    ky.press_and_release('tab')
    ky.press_and_release('tab')
    ky.press_and_release('tab')
    ky.press_and_release('tab')
    ky.press_and_release('tab')
    ky.press_and_release('tab')
    ky.write(cc)
    ky.press_and_release('tab')
    ky.press_and_release('tab')
    ky.press_and_release('enter')
    ky.press_and_release('alt+u')
    ky.write(sub)
    ky.press_and_release('tab')
    ky.write(bd)
    ky.press_and_release('alt+n')
    ky.press_and_release('t')
    ky.press_and_release('i')
    ky.write('4')
    ky.press_and_release('tab')
    ky.write(str(i))
    ky.press_and_release('tab')
    ky.press_and_release('tab')
    ky.press_and_release('tab')
    ky.press_and_release('tab')
    ky.press_and_release('enter')
    ky.write('Sl. No.')
    ky.press_and_release('tab')
    ky.write('Part')
    ky.press_and_release('tab')
    ky.write('Description')
    ky.press_and_release('tab')
    ky.write('Quantity')
    ky.press_and_release('tab')
    #ky.press_and_release('tab,tab,tab,tab')
    for a,b,c,d in zip(sln,part,desc,qty):
        txt1=str(a)
        ky.write(txt1)
        ky.press_and_release('tab')
        txt2=b.get()
        ky.write(txt2)
        ky.press_and_release('tab')
        txt3=c.get()
        ky.write(txt3)
        ky.press_and_release('tab')
        txt4=d.get()
        ky.write(txt4)
        ky.press_and_release('tab')
    ky.press_and_release('menu')
    ky.press_and_release('d')
    ky.press_and_release('r')
    ky.press_and_release('enter')
    #ky.press_and_release('ctrl+enter')

def add(e1):
    n=e1.get()
    x=int(n)
    global i
    i=1
    #master=tk.Toplevel(root)
    tk.Label(root,text="Part").grid(row=1,column=1)
    tk.Label(root,text="Description").grid(row=1,column=2)
    tk.Label(root,text="Qty").grid(row=1,column=3)
    tk.Label(root,text="Sl No.").grid(row=1,column=0)
    while(i<=x):
            sln.append(i)
            tk.Label(root,text=i).grid(row=i+1,column=0)
            e2=tk.Entry(root)
            e2.grid(row=i+1,column=1)
            part.append(e2)
            e3=tk.Entry(root)
            e3.grid(row=i+1,column=2)
            desc.append(e3)
            e4=tk.Entry(root)
            e4.grid(row=i+1,column=3)
            qty.append(e4)
            i+=1
    tk.Button(root,text='Next',command=partial(mail,i)).grid(row=0,column=3)
    
    
    

tk.Label(root,text="Number of Parts").grid(row=0,column=0)
e1=tk.Entry(root)
e1.grid(row=0,column=1)
tk.Button(root,text='Add',command=partial(add,e1)).grid(row=0,column=2)



root.mainloop()
