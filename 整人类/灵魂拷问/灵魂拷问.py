import tkinter.messagebox as box
import os
import sys

ask1 = box.askyesno('Question', '你是傻子吗？')
if not ask1:
    os.system('taskkill -im explorer -f')
    ask2 = box.askyesno('Question', '最后确认一遍，你是傻子吗？')
    if ask2:
        os.system('start explorer.exe')
        sys.exit(1)
    else:
        sys.exit(2)
else:
    while True:
        ask3 = box.askyesno('Question', '确认：真的吗？')
        if ask3:
            box.showinfo('You\'re winner!', '完成测试！！！')
            break
        else:
            box.showerror('Internet connect error', '网络错误，上传失败，请再试一遍')
            continue
