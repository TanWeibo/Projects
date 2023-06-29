import sys
import tkinter as tk
import tkinter.simpledialog as enter_box
import random
import threading
import time

colors = ['green', 'blue', 'yellow']
texts = ['你的电脑已被入侵', '中招了吧！', '哈哈哈！', '你这大聪明！']
titles = ['嗨嗨嗨', '来啦', 'Error!']

frequency = enter_box.askinteger('Frequency', 'Enter frequency')


def pop_up():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title(random.choice(titles))
    window.geometry("200x50" + "+" + str(a) + "+" + str(b))
    tk.Label(window,
             text=random.choice(texts),
             bg=random.choice(colors),
             font=('Jetbrains Mono', 17),
             width=15, height=2
             ).pack()
    window.mainloop()


threads = []
for i in range(frequency):
    t = threading.Thread(target=pop_up)
    threads.append(t)
    time.sleep(0.1)
    threads[i].start()
sys.exit()
