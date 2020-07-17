import pyautogui
import os
import tkinter as tk
import win32gui, keyboard, time
import xlrd


ExcelFileName= 'meh.xlsx'
workbook = xlrd.open_workbook(ExcelFileName)
worksheet = workbook.sheet_by_name("Sheet3") # We need to read the data 
#from the Excel sheet named "Sheet1"
nr = worksheet.nrows #Number of Rows
print(nr)

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



root = tk.Tk()
frame = tk.Frame(root)
frame.grid()


button = tk.Button(frame,text="CLOSE PULSE POP UP",fg="red",command=close_pulse)
#button.pack()
button.grid(row=0,column=1)
button = tk.Button(frame,text="DO NOT SLEEP",fg="red",command=no_sleep)
#button.pack()
button.grid(row=1,column=1)
i=1
y='.png'
cl=0
rw=2
tc=20
while(i<=tc):
    img="{}{}".format(i, y)
    ph=tk.PhotoImage(file=img)
    label=tk.Label(image=ph)
    label.image=ph
    #label.pack()
    print(img)
    button = tk.Button(image=ph,width="180",height="50",command=root.destroy)
    #button.pack(ipadx=10,ipady=10)
    #button.pack()
    #button.config(image=tk.PhotoImage(file=img),width="750",height="80")
    #button.grid(row=3,column=1)
    for cl in 
    if (cl%2==0):
        if(rw%2!=0):
            #button.pack(side=tk.LEFT)
            #button.place(x=i*150,y=i*50)
            button.grid(row=rw,column=cl+1)
        else:
            #button.pack(side=tk.LEFT)
            #button.place(x=i*150,y=i*50)
            button.grid(row=rw,column=cl)
    
    if (cl==0 and i<=tc):
       cl=cl
    else:
        if (cl%10==0):
            cl =cl+1
    
    rw=rw+1
    i=i+1
    
        
root.mainloop()
