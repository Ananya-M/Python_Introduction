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
#print(sml)     



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

def copy_img(j):
    sm=sml[j]
    pyperclip.copy(sm)
        

root = tk.Tk()
frame = tk.Frame(root)
frame.grid()


button = tk.Button(frame,text="CLOSE PULSE POP UP",fg="red",command=close_pulse)
button.grid(row=0,column=1)
button = tk.Button(frame,text="DO NOT SLEEP",fg="red",command=no_sleep)
button.grid(row=1,column=1)

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
            button = tk.Button(text=sml[i],width=25,command=partial(copy_img,j))
            button.grid(row=rw,column=cl)
            i=i+1
            j=j+1
        rw=rw+1 
    rw=2
    cl =cl+1
button = tk.Button(root,text="CLOSE",fg="red",command=root.destroy)
button.grid(row=12,column=0)

root.mainloop()
