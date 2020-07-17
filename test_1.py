import os
import xlsxwriter
import tkinter as tk

def create():
    path=e2.get()
    name=e1.get()
    x="{}{}{}".format(path,name,".xlsx")
    print(x)
    fd = os.open(x, x)
    #os.write(fd, abcd )
    os.close( fd )
    #workbook = xlsxwriter.Workbook(x)
    #worksheet = workbook.add_worksheet()
    open(x)
    
master=tk.Tk()
tk.Label(master, text="New file name").grid(row=1)
tk.Label(master, text="Enter Path").grid(row=2)
e1=tk.Entry(master)
e2=tk.Entry(master)
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
tk.Button(master, text='Create', command=create).grid(row=3,column=1,pady=4)
tk.Button(master, text='Close', command=master.destroy).grid(row=3,column=2)
master.mainloop()
