import win32gui, keyboard, time
 
def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
 
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
keyboard.press_and_release('alt+f')
keyboard.press_and_release('m')
keyboard.press_and_release('t')
keyboard.write('20031748')
