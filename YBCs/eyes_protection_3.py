import time
import FirstUse
import os
import tkinter.messagebox as info

remind_time = FirstUse.active()
start = info.askyesno('启动', '你想要现在启动吗？')
if start:
    print(remind_time)
    time.sleep(int(remind_time))
    info.showinfo('时间到！', '时间到了，你的电脑将锁定')
    os.system('Rundll32.exe user32.dll,LockWorkStation')
