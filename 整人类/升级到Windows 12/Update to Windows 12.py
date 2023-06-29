import tkinter.simpledialog as enter_box
import tkinter.messagebox as box
import time
import os
import random
import easygui

view_protocol = False
viewing_protocol_time = 0
file = open('H:/Projects/整人类/升级到Windows 12/协议.txt', 'r', encoding='utf-8')
protocol = file.read()
file.close()
while True:
    agree = enter_box.askstring('Update to Windows 12', '您是否同意协议？[输入“同意”、“不同意”、“查看协议”]')
    if agree == '同意':
        if view_protocol and viewing_protocol_time >= 10:
            box.showinfo('INFO', '按下“确定”一开始检测安装环境')
            for progress in range(1, 101):
                print(f"""当前进度：%{progress}""")
                time.sleep(0.45)
                os.system('cls')
            print('下一步')
            time.sleep(5)
            for progress in range(1, 101):
                print(f"""当前进度：%{progress}""")
                time.sleep(random.randint(1, 5 + 1))
                os.system('cls')
            print('正在检查系统', end='')
            for i in range(6):
                print('.', end='')
            box.showwarning('WARNING', '系统版本过低，请升级到Windows 12!!!')
            break
        elif not view_protocol:
            box.showwarning('WARNING', '请查看协议！')
            continue
        elif viewing_protocol_time < 10:
            box.showwarning('WARNING', '请认真查看协议！')
            continue
    elif agree == '不同意':
        no_agree_choice = easygui.buttonbox('请选择操作', 'CHOICE', ['回到初始界面', '退出'])
        if no_agree_choice == '回到初始界面':
            continue
        elif no_agree_choice == '退出' or no_agree_choice is None:
            break
        else:
            break
    elif agree == '查看协议':
        view_protocol = True
        viewing_start = time.perf_counter()
        box.showinfo('协议', protocol)
        viewing_end = time.perf_counter()
        viewing_protocol_time = viewing_end - viewing_start
    else:
        continue
