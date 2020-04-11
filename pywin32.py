import win32api, win32con
import time
def click(x,y):
    win32api.SetCursorPos((0,0))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.SetCursorPos((x,y))
    time.sleep(5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
click(150,100)
