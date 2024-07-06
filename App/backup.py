def main(head, feet):
    chickens = int((4 * head - feet) / 2)
    try:
        if head != 0 and (4 * head - feet) % (chickens * 2) == 0:
            rabbits = int(head - chickens)
            if chickens < 0 or rabbits < 0:
                box.showerror('无解', f'{head}个头，{feet}只脚的题目无解')
            else:
                box.showinfo('结果', f'鸡有{str(chickens)}只，兔子有{str(rabbits)}只')
        else:
            box.showerror('无解', f'{head}个头，{feet}只脚的题目无解')
    except ZeroDivisionError:
        box.showerror('无解', f'{head}个头，{feet}只脚的题目无解')


enter_head = enter_box.askinteger('输入', '头的数量', minvalue=1)
enter_feet = enter_box.askinteger('输入', '脚的数量', minvalue=enter_head)
main(enter_head, enter_feet)