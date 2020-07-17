import tkinter as tk



def write_slogan():
    master = tk.Tk()
    whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
    msg = tk.Message(master, text = whatever_you_do)
    msg.config(bg='lightgreen', font=('times', 24, 'italic'))
    msg.pack()
    tk.mainloop()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,text="QUIT",fg="red",command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,text="Hello",command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()
