import openpyxl as xl
import time
import keyboard as ky
import tkinter as tk
from functools import partial
import win32com.client
from win32com.client import Dispatch, constants
from tkinter.filedialog import askopenfilename
import pandas as pd



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
    tk.Label(master,text="No of Attachments:").grid(row=3,column=0)
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
    fc=e101.get()
    ct=int(fc)
    data={'Sl. No.':[],'Part':[],'Description':[],'Quantity':[]}
    print(type(data))
    l=0
    while (l<len(sln)):
        a=sln[l]
        b=part[l].get()
        c=desc[l].get()
        d=qty[l].get()
        #data={'Sl. No.':[a],'Part':[b],'Description':[c],'Quantity':[d]}
        data['Sl. No.'].append(a)
        data['Part'].append(b)
        data['Description'].append(c)
        data['Quantity'].append(d)
        print(type(data),len(sln))
        #li=list(data)
        #li.append(li)
        #print(type(li))
        #data_tl=tuple(data_li)
        #print("data:",data)
        l+=1
    print(data)
    table=pd.DataFrame(data)
    body='<html><body>' + "Hello,"+'<br/>'+"Please send us a quote for the below parts."+'<br/>'+table.to_html(index=False) + '</body></html>'
    
    const=win32com.client.constants
    olMailItem = 0x0
    obj = win32com.client.Dispatch("Outlook.Application")
    newMail = obj.CreateItem(olMailItem)
    newMail.To = to
    newMail.Cc=cc 
    newMail.Subject = sub
    newMail.HTMLBody = body
    newMail.BodyFormat = 2 # olFormatHTML https://msdn.microsoft.com/en-us/library/office/aa219371(v=office.11).aspx
   
    k=1
    while (k<=ct):
        att_f=askopenfilename()
        print(att_f)
        newMail.Attachments.Add(Source=att_f)
        k+=1
    
    
        
    newMail.display()
    
    
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
