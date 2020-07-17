import pyautogui
import os
import tkinter as tk
import win32gui, keyboard, time
import pyperclip
from functools import partial
import os, mouse as mo
import win32gui, keyboard as kb, time
from tkinter import filedialog
rp = "\\\\vssstorage\\UTCMechanical\\Nithish\\MAT'L"
path="\\\\vssstorage\\UTCMechanical\\Anil\\PPT.pptm"
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

array2 = next(os.walk(rp))[1]
array3 = []
print(array2)
for local_folder in array2:
   array3.append( os.path.abspath(os.path.join(rp, local_folder)))
print(array3)
    
root = tk.Tk()
root.title("GUI")

def open_folders(a):
    sp=a
    path=os.path.realpath(sp)
    os.startfile(path)

def ref_mat():
    root2 = tk.Toplevel(root)
    root2.title("Reference Material")
    root2.grab_set()
    tk.Label(root2,text="Choose the folder",justify = tk.LEFT,padx = 20).pack()
    i=0
    n=len(array2)
    while (i<n ):
            a=array3[i]
            tk.Button(root2, text=array2[i],command=partial(open_folders,a)).pack()
            i=i+1
    #root2.mainloop()


def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def ppt():
    kb.press_and_release('win+d')
    time.sleep(0.2)
   

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
    kb.press_and_release('alt+space,x')
    time.sleep(1)
    kb.press_and_release('win+PrtScn')

    kb.press_and_release('win+r')
    time.sleep(.1)
    kb.write(path)
    kb.press_and_release('enter')
    time.sleep(5)
    kb.press_and_release('end')
    kb.press_and_release('alt+H,y')
    kb.press_and_release('ctrl+v')
    kb.press_and_release('ctrl+s')
    mo.move(700, 500, absolute=True, duration=0)
    mo.click(button='left')
    mo.click(button='right')
    kb.press_and_release('k,k')

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






button = tk.Button(root,text="CLOSE PULSE POP UP",fg="red",command=close_pulse).grid(row=0,column=1)
button = tk.Button(root,text="DO NOT SLEEP",fg="red",command=no_sleep).grid(row=1,column=1)
button = tk.Button(root,text="SMILEY",fg="red",command=smiley).grid(row=2,column=1)
button = tk.Button(root,text="Delay shut",fg="red",command=shut_down).grid(row=3,column=1)
#button = tk.Button(root,text="SCREEN SHOT",fg="red",command=ppt).grid(row=4,column=1)
button = tk.Button(root,text="Reference Material",fg="red",command=ref_mat).grid(row=4,column=1)
button = tk.Button(root,text="CLOSE",fg="red",command=root.destroy).grid(row=5,column=1)




root.mainloop()
