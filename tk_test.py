import tkinter as tk

def show_entry_fields():
    mt = tk.Tk()
    show_enrty = "e1, e2"
    msg = tk.Message(mt, text = (e1.get(), e2.get()))
    msg.config(bg='lightgreen', font=('times', 24, 'italic'))
    msg.pack()
    tk.mainloop()

master = tk.Tk()
tk.Label(master, text="First Name").grid(row=0)
tk.Label(master, text="Last Name").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master, text='Quit', command=quit).grid(row=3, column=0,  pady=4)
tk.Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1,  pady=4)

master.mainloop( )
