import openpyxl as xl
import win32gui, os, time
import keyboard as ky
import tkinter as tk
from functools import partial
import win32com.client
from win32com.client import Dispatch, constants
from tkinter.filedialog import askopenfilename



root=tk.Tk()
root.title("Create RFQ Mail")

sln=[]
part=[]
desc=[]
qty=[]
bd="Hello,\nPlease send us a quote for the below parts.\n\r"


def mail(i):
    master=tk.Toplevel(root)
    tk.Label(master,text="To:").grid(row=0,column=0)
    tk.Label(master,text="Cc:").grid(row=1,column=0)
    tk.Label(master,text="Subjet:").grid(row=2,column=0)
    tk.Label(master,text="Attachemnt:").grid(row=3,column=0)
    e98=tk.Entry(master)
    e98.grid(row=0,column=1)
    e99=tk.Entry(master)
    e99.grid(row=1,column=1)
    e100=tk.Entry(master)
    e100.grid(row=2,column=1)
    e101=tk.Entry(master)
    e101.grid(row=3,column=1)
    tk.Button(master,text='Next',command=partial(outlook,e98,e99,e100,e101,i)).grid(row=4,column=0)
    tk.Button(master,text='Close',command=master.destroy).grid(row=4,column=1)
    
    
    


def outlook(e98,e99,e100,e101,i):
    to=e98.get()
    cc=e99.get()
    sub=e100.get()
    #att_f=e101.get()
    att_f=askopenfilename()
    print(att_f)
    #path=att_f.replace("\\","\\\\")
    #print(path)
    const=win32com.client.constants
    olMailItem = 0x0
    obj = win32com.client.Dispatch("Outlook.Application")
    newMail = obj.CreateItem(olMailItem)
    newMail.Subject = sub
    # newMail.Body = "I AM\nTHE BODY MESSAGE!"
    newMail.BodyFormat = 2 # olFormatHTML https://msdn.microsoft.com/en-us/library/office/aa219371(v=office.11).aspx
    newMail.HTMLBody = bd
    newMail.To = to
    newMail.Cc=cc
    #attachment1 = r"C:\Users\Public\Pictures\Sample Pictures\Jellyfish.jpg"
    newMail.Attachments.Add(Source=att_f)
    newMail.display()
    ky.pre
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
    #newMail.send()

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
tk.Button(root,text="Close",command=root.destroy).grid(row=0, column=4)
root.mainloop()
