import tkinter.simpledialog as enter
import tkinter.messagebox as info

def active(first=False):
    file = open('Set.dll', 'r')
    state = file.readlines()
    state = state[0]
    if state == 'FirstUse' or first:
        while True:
            remind_time = enter.askinteger('初次使用配置', '这是初次使用配置页面,你想要隔多少时间提醒？(以秒做单位)',
                                       minvalue=300)
            if remind_time is None:
                info.showerror('error', '值不能为None，请重新输入！！！')
            else:
                break
        file.close()
        file = open('Set.dll', 'w')
        file.write(f'Used\n{remind_time}')
        file.close()
        info.showinfo('配置', '配置成功！')
    else:
        file = open('Set.dll', 'r')
        remind_time = file.readlines()
        remind_time = remind_time[1]
        file.close()
    return remind_time
