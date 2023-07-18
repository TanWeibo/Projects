from pyperclip import copy, paste
import tkinter.messagebox as box
import os

box.showinfo('INFO', '按下确定即开始运行本程序。')
copy('剪切板已经罢工了！！！')
while True:
    try:
        now = paste()
        if now != '剪切板已经罢工了！！！':
            copy('剪切板已经罢工了！！！')
    except KeyboardInterrupt:
        print('Thanks!')
        os.system('pause')
        break
