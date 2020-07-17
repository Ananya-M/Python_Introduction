import pyautogui
import os
import tkinter as tk
import win32gui, keyboard, time
import pyperclip
from functools import partial

sml=["¯\_(ツ)_/¯",
"( ͡° ͜ʖ ͡°)",
"ಠ_ಠ",
"(╯°□°）╯︵ ┻━┻",
"┻━┻ ︵ ヽ(°□°ヽ)",
"┻━┻ ︵ ＼( °□° )／ ︵ ┻━┻",
"┬─┬ノ( º _ ºノ)",
"(ﾉಥ益ಥ）ﾉ ┻━┻",
"┬──┬ ¯\_(ツ)",
"┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻",
"┻━┻ ︵ ¯\(ツ)/¯ ︵ ┻━┻",
"(╯°Д°）╯︵ /(.□ . \)",
"ʕノ•ᴥ•ʔノ ︵ ┻━┻",
"┌∩┐(◣_◢)┌∩┐",
"ლ(ಠ益ಠ)ლ",
"(ง’̀-‘́)ง",
"(ಠ_ಠ)",
"╭∩╮（︶︿︶）╭∩╮ ",
"(ᵔᴥᵔ)",
"(=^ェ^=)",
"ʕ •ᴥ•ʔ",
"（・⊝・）",
"=＾● ⋏ ●＾=",
"( 。・_・。)人(。・_・。 )",
"└(^o^ )Ｘ( ^o^)┘",
"(✿◠‿◠)",
"(｡◕‿◕｡)",
"ヽ༼ຈل͜ຈ༽ﾉ",
"(づ｡◕‿‿◕｡)づ",
"~(˘▾˘~)",
"ヘ( ^o^)ノ＼(^_^ )",
"(. ❛ ᴗ ❛.)",
"｡^‿^｡",
"( ͡ᵔ ͜ʖ ͡ᵔ )",
"☉_☉",
"¯\(°_o)/¯",
"(゜-゜)",
"(・_・ヾ",
"o_O",
"(¬_¬)",
"( ͡° ʖ̯ ͡°)",
"╮ (. ❛ ᴗ ❛.) ╭",
"(•_•) ( •_•)>⌐■-■ (⌐■_■)",
"(▀̿Ĺ̯▀̿ ̿)"]
    



def close_pulse():
    os.system("taskkill /f /im  WinFormDemo.exe")

def no_sleep():
    try:
       while True:
           pyautogui.moveTo(100, 100, duration=0.05)
           pyautogui.press("shift")
           pyautogui.moveTo(200, 100, duration=0.05)
           pyautogui.press("shift")
           pyautogui.moveTo(200, 200, duration=0.05)
           pyautogui.press("shift")
           pyautogui.moveTo(100, 200, duration=0.05)
           pyautogui.press("shift")
    except:
       pyautogui.press('enter')

def copy_img(j):
    sm=sml[j]
    pyperclip.copy(sm)
        
def smiley():
    branch = tk.Toplevel(root)
    branch.title("SMILEY")
    branch.grab_set()
    nr=43
    i=0
    j=0
    y='.png'
    cl=0
    rw=2
    q=nr//10
    while (cl<=q+1):
        while(rw<=11):
            if(i<=nr):
                button = tk.Button(branch,text=sml[i],width=25,command=partial(copy_img,j))
                button.grid(row=rw,column=cl)
                i=i+1
                j=j+1
            rw=rw+1 
        rw=2
        cl =cl+1
    button = tk.Button(branch,text="CLOSE",fg="red",command=branch.destroy)
    button.grid(row=12,column=0)

def shut_down():
    root2=tk.Toplevel(root)
    root2.title("Shut Down?")
    root2.grab_set()
    tk.Label(root2,text="Do you want to shut down this machine?").grid(row=0)
    tk.Button(root2, text='Yes', command=partial(delay)).grid(row=1, column=0,  pady=4)
    tk.Button(root2, text='No', command=root2.destroy).grid(row=1, column=1,  pady=4)

def delay():
    branch2=tk.Toplevel(root)
    branch2.title("Delay")
    branch2.grab_set()
    tk.Label(branch2, text="Enter time in minutes:").grid(row=0)
    e1 = tk.Entry(branch2)
    e1.grid(row=0, column=1)
    tk.Button(branch2, text='Run', command=partial(shut,e1)).grid(row=4, column=1,  pady=4)
    tk.Button(branch2, text='Close', command=branch2.destroy).grid(row=4, column=2,  pady=4)
    
def shut(e1):
    mins=float(e1.get())
    secs=mins*60
    time.sleep(secs)
    os.system("shutdown /s /t 1");


    
root = tk.Tk()
root.title("GUI")
frame = tk.Frame(root)
frame.grid()


button = tk.Button(frame,text="CLOSE PULSE POP UP",fg="red",command=close_pulse)
button.grid(row=0,column=1)
button = tk.Button(frame,text="DO NOT SLEEP",fg="red",command=no_sleep)
button.grid(row=2,column=1)
button = tk.Button(frame,text="SMILEY",fg="red",command=smiley)
button.grid(row=4,column=1)
button = tk.Button(frame,text="Delay shut",fg="red",command=shut_down)
button.grid(row=6,column=1)
button = tk.Button(frame,text="CLOSE",fg="red",command=root.destroy)
button.grid(row=8,column=1)



root.mainloop()
