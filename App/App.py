import tkinter.messagebox as box
import tkinter.simpledialog as enter_box
import easygui
import random
import requests
import os
from pythonping import ping
from datetime import datetime
import time
import sys
from colorama import Fore, Back, Style

normalRun = False
try:
    file_sleepTime = open('H:/Projects/App/Setting Files/End_Sleep_Time.App-Setting', 'r')
    end_sleep_time = int(file_sleepTime.read())
    file_sleepTime.close()
except ValueError:
    file_sleepTime = open('H:/Projects/App/Setting Files/End_Sleep_Time.App-Setting', 'w')
    print('请稍后，程序正在恢复文件...')
    file_sleepTime.write('5')
    end_sleep_time = 5
    file_sleepTime.close()
except FileNotFoundError:
    if len(sys.argv) != 2:
        box.showwarning('警告', '找不到设置文件，请按H:/Projects/App/Help/Helps.txt解决！')
        sys.exit(1)
    elif len(sys.argv) == 2:
        if sys.argv[1].lower() == 'normalrun':
            print('你现在处于NormalRun模式')
            end_sleep_time = 5
            normalRun = True
        else:
            print('无效参数！')
            end_sleep_time = 5
except Exception:
    print('未知错误，end_sleep_time将会=5')
    end_sleep_time = 5

start_time = time.perf_counter()
morse_codes = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": ".-",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--.."
}
if normalRun:
    version = """NiceProgram App VERSION 1.3
处于NormalRun模式"""
elif not normalRun:
    version = 'NiceProgram App VERSION 1.3'
print(Fore.BLUE + '*:这是输出区，在使用Ping等功能时，返回结果将显示在这里。')
print(Style.RESET_ALL)
while True:
    Home_Choice = easygui.buttonbox('选择一个功能', '主页',
                                    ['猜数字', '中英互译机', 'Ping', '石头剪刀布', '进制转换', '让你的设备蓝屏'
                                        , '摩斯密码转换器', '计算正确率', '计算平均数', 'Preview', '恶搞', '读心术',
                                     '计算鸡兔同笼问题', 'Collatz数列', '激活Windows(需要管理员权限)', '九九乘法表',
                                     'BMI检测',
                                     '关于', '退出'])
    if Home_Choice == '猜数字':
        scope = enter_box.askstring('输入范围', '输入范围，中间用“~”分隔')
        find_to = scope.find('~')
        try:
            start = int(scope[:find_to])
            end = int(scope[find_to + 1:])
        except ValueError:
            box.showerror('数值错误', '你输入的不是数/整数！')
        else:
            right = random.randint(start, end)
            Error_frequency = 0
            while True:
                try:
                    Guess_numbers_Enter = enter_box.askstring('输入', f"""计算机已经创建了{start}~{end}中的数字，尽你的能力猜到它！
输入exit退出
输入empty清空所有数据""")
                    if Guess_numbers_Enter != 'exit' and Guess_numbers_Enter != 'empty':
                        Guess_numbers_Enter = int(Guess_numbers_Enter)
                        if start <= Guess_numbers_Enter <= end:
                            if Guess_numbers_Enter == right:
                                box.showinfo('猜对了！', f'恭喜你猜对了！你一共用了{Error_frequency}次。')
                                try:
                                    file_guessNumber = open('H:/Projects/App/GuessNumbers/GuessNumbers.txt', 'a')
                                except FileNotFoundError:
                                    box.showerror('找不到文件', '找不到文件！')
                                    break
                                except Exception:
                                    box.showerror('错误', '未知错误。')
                                    break
                                else:
                                    file_guessNumber.write('\n')
                                    file_guessNumber.write(f"""错误次数：{str(Error_frequency)}
日期：{datetime.today()}
范围：{str(start)}~{str(end)}
------""")
                                    file_guessNumber.close()
                                    break
                            elif Guess_numbers_Enter > right:
                                Error_frequency += 1
                                box.showerror('输入错误', '太大啦！')
                                continue
                            elif Guess_numbers_Enter < right:
                                Error_frequency += 1
                                box.showerror('输入错误', '太小啦！')
                        else:
                            box.showerror('超出范围', '输入的数值超出范围！')
                            continue
                    elif Guess_numbers_Enter == 'exit':
                        break
                    elif Guess_numbers_Enter == 'empty':
                        file_sleepTime = open('H:/Projects/App/GuessNumbers/GuessNumbers.txt', 'w')
                        file_sleepTime.write('GuessNumber FREQUENCY')
                        file_sleepTime.close()
                        break
                except ValueError:
                    box.showerror('数值错误', '你输入的不是数！')
                    continue
                except Exception:
                    box.showerror('错误', '未知错误')
    elif Home_Choice == '中英互译机':
        string = enter_box.askstring('翻译', '输入翻译内容')
        data = {
            'doctype': 'json',
            'type': 'AUTO',
            'i': string
        }
        try:
            translate_url = 'http://fanyi.youdao.com/translate'
            r = requests.get(translate_url, params=data)
            result = r.json()
            translate_result = result['translateResult'][0][0]["tgt"]
            box.showinfo('翻译结果', translate_result)
        except Exception:
            box.showerror('错误', '无法翻译，可能是因为在当前状态下无Internet连接，请连接Internet后再试')
    elif Home_Choice == 'Ping':
        Ping_Choice = easygui.buttonbox('选择方式', 'Ping',
                                        ['使用系统Ping(仅限Windows，其它系统使用会报错)', '使用Python Ping'])
        if Ping_Choice == '使用系统Ping(仅限Windows，其它系统使用会报错)':
            System_url = enter_box.askstring('输入', '请输入网址')
            try:
                System_Ping = os.system(f'Ping {System_url}')
                print(System_Ping)
                print('结束')
            except Exception:
                box.showerror('错误',
                              '调用系统Ping时错误，请检查系统是否是Windows(或者Windows版本低于Windows 98)，或者是Ping时发生其他错误')
        elif Ping_Choice == '使用Python Ping':
            Python_ping_url = enter_box.askstring('输入', '请输入网址')
            Python_ping = str(ping(Python_ping_url))
            print(Python_ping)
            print('结束')
    elif Home_Choice == '石头剪刀布':

        def show_state(now_state):
            if now_state == 'win':
                box.showinfo('NICE!', '你赢了！牛逼！')
            elif now_state == 'lose':
                box.showinfo('再接再厉！', '你输了。再接再厉！')
            elif now_state == 'tie':
                box.showinfo('打平了', '打平了，旗鼓相当。')


        win = 0
        lose = 0
        tie = 0
        while True:
            FingerGuessing_list = ['石头', '剪刀', '布']
            if win == 0 and lose == 0 and tie == 0:
                message = f"""选择一个选项
当前状态：
待开始游戏......"""
            else:
                message = f"""选择一个选项
当前状态：
赢:{str(win)} 输:{str(lose)} 平局:{str(tie)}"""
            Your_Choice = easygui.buttonbox(message, '选择', FingerGuessing_list)
            System_Choice = random.choice(FingerGuessing_list)
            if Your_Choice == '石头':
                if System_Choice == '石头':
                    show_state('tie')
                    tie += 1
                    continue
                elif System_Choice == '剪刀':
                    show_state('win')
                    win += 1
                    continue
                elif System_Choice == '布':
                    show_state('lose')
                    lose += 1
                    continue
            elif Your_Choice == '剪刀':
                if System_Choice == '石头':
                    show_state('lose')
                    lose += 1
                    continue
                elif System_Choice == '剪刀':
                    show_state('tie')
                    tie += 1
                    continue
                elif System_Choice == '布':
                    show_state('win')
                    win += 1
                    continue
            elif Your_Choice == '布':
                if System_Choice == '石头':
                    show_state('win')
                    win += 1
                    continue
                elif System_Choice == '剪刀':
                    show_state('lose')
                    lose += 1
                    continue
                elif System_Choice == '布':
                    show_state('tie')
                    tie += 1
                    continue
            elif Your_Choice is None:
                if win == 0 and lose == 0 and tie == 0:
                    break
                else:
                    if win > lose:
                        state = '赢'
                    elif win == lose:
                        state = '平局'
                    elif win < lose:
                        state = '输'
                    try:
                        GuessFist_file = open('H:/Projects/App/GuessFist/GuessFist.txt', 'a')
                    except FileNotFoundError:
                        box.showerror('保存失败', '没有找到文件。')
                    else:
                        GuessFist_file.write('\n')
                        GuessFist_file.write(f"""赢:{win}
输:{lose}
平局:{tie}
综合:{state}
时间：{datetime.today()}""")
                        GuessFist_file.write('\n----------------')
                    finally:
                        GuessFist_file.close()
                        break
    elif Home_Choice == '进制转换':
        JinZhi_Choice = easygui.buttonbox('选择一个选项', '进制转换', ['十进制转二进制', '几进制转十进制'])
        if JinZhi_Choice == '十进制转二进制':
            while True:
                JinZhi_Enter = enter_box.askstring('输入数字', '请输入一个十进制数字')
                try:
                    binary = bin(int(JinZhi_Enter))
                    binary = str(binary)
                    binary = binary.replace('0b', '')
                    box.showinfo('结果', f'此二进制数是：{binary}')
                    break
                except ValueError:
                    box.showerror('错误', '请确保你输入的内容是数字！')
                    continue
                except Exception:
                    box.showerror('意想不到的事发生了！', '程序发生了未知错误！')
                    break
        elif JinZhi_Choice == '几进制转十进制':
            while True:
                JinZhi_Enter = enter_box.askstring('输入数字', '输入一个任意进制的数字')
                what_JinZhi = enter_box.askstring('输入进制', '请输入你刚刚输入的数字的进制')
                try:
                    what_JinZhi = int(what_JinZhi)
                    outcome = int(JinZhi_Enter, what_JinZhi)
                    box.showinfo('结果', str(outcome))
                    break
                except ValueError:
                    box.showerror('错误', '请确保你输入的内容是数字！')
                    continue
                except Exception:
                    box.showerror('意想不到的事发生了！', '程序发生了未知错误！')
                    break
    elif Home_Choice == '让你的设备蓝屏':
        box.showwarning('警告', """仅限Windows !
这可不是开玩笑，此功能真的会让Windows 蓝屏！！！
Windows 11加了保护措施，不能蓝屏......""")
        continue_choice = box.askyesno('继续？', '真的要继续吗？')
        if continue_choice:
            continue_enter = enter_box.askstring('验证', """如需继续，请输入“yes”
输入yes后如需取消，请按下Ctrl(Command)+C。""")
            if continue_enter == 'yes':
                try:
                    print(Back.RED + Fore.GREEN + '3')
                    time.sleep(1)
                    print(2)
                    time.sleep(1)
                    print(1)
                    print(Style.RESET_ALL)
                    time.sleep(1)
                    os.system('taskkill -im svchost.exe -f')
                except KeyboardInterrupt:
                    print('紧急取消完成。' + Style.RESET_ALL)
            else:
                pass
        else:
            pass
    elif Home_Choice == '摩斯密码转换器':
        while True:
            letter_enter = enter_box.askstring('Enter', '''输入要转换成摩斯密码的字母，只能输入小写！否则程序将不返回大写字母、特殊符号
输入“EXIT退出”''')
            if letter_enter != 'EXIT':
                length = len(letter_enter)
                morse_code = ''
                for i in range(length):
                    if letter_enter[i] in morse_codes.keys():
                        morse_code = morse_code + '   ' + morse_codes.get(letter_enter[i])
                box.showinfo('result', f'转换完成！结果：{morse_code}')
            elif letter_enter == 'EXIT':
                break
    elif Home_Choice == '计算正确率':
        all_questions = enter_box.askinteger('计算正确率', '输入题目总数')
        right_questions = enter_box.askinteger('计算正确率', '输入正确题目总数')
        accuracy = right_questions / all_questions * 100
        if accuracy < 0 or accuracy > 100:
            accuracy = str(right_questions / all_questions * 100) + '%'
            box.showerror('错误的结果', f"""计算逻辑错误:
超出范围。
错误结果:{accuracy}""")
        else:
            accuracy = str(right_questions / all_questions * 100) + '%'
            box.showinfo('正确率', f'正确率：{accuracy}')
    elif Home_Choice == '计算平均数':
        numbers = []
        while True:
            number = enter_box.askstring('计算平均数', '请输入一个数字，输入"start"开始计算，输入"exit"退出')
            if number == 'exit':
                numbers = []
                break
            elif numbers == [] and number == 'start':
                box.showerror('错误', '请输入数字！')
                continue
            elif number != 'exit' and number != 'start':
                try:
                    number = int(number)
                except ValueError:
                    box.showwarning('错误', '请输入整数！输入小数将去小数点及小数！')
                    continue
                except Exception:
                    box.showerror('意想不到的事发生了！', '未知错误。')
                    numbers = []
                    break
                else:
                    numbers.append(number)
            elif len(numbers) > 0 and number != 'exit' and number == 'start':
                number_sum = sum(numbers)
                average = number_sum / len(numbers)
                box.showinfo('平均数', f'它们的平均数为：{average}')
                numbers = []
    elif Home_Choice == 'Preview':
        hide_enter = input('Enter the preview function name:Enter "EXIT" to exit.')
        if hide_enter == 'Talk out':
            print("""Talk out:
If you are happy,you can enter "EXIT" to exit.""")
            __sos__ = 0
            while True:
                talk_out = input()
                if talk_out == 'EXIT':
                    os.system('cls')
                    yes = input('Do you want exit?(Enter "yes" or "no".)')
                    if yes == 'yes':
                        os.system('cls')
                        break
                    else:
                        continue
                elif talk_out == 'sos' and __sos__ <= 2:
                    __sos__ += 1
                elif talk_out == 'sos' and __sos__ == 3:
                    print('SORRY,I CANNOT HELP YOU.Don\'t forget.I am just a program.')
        elif hide_enter == 'EXIT':
            os.system('cls')
            continue
    elif Home_Choice == '恶搞':
        os.system('taskkill -im explorer.exe -f')
        os.system('Shutdown -s -t 60 -c 你的电脑将会在60秒后关机，哈哈哈！想恢复就点击确定，在弹出的窗口中输入密码！！！')
        while True:
            password = enter_box.askstring('Password', '快输密码！')
            if password == 'Twb20131023':
                os.system('Shutdown -a')
                os.system('Explorer.exe')
                break
            else:
                box.showerror('错误', '密码错误！')
    elif Home_Choice == '读心术':
        box.showinfo('欢迎', '请你想一个1~31的数字，开始吧！！！')
        right = []
        pow = 1
        result = 0
        for i in range(1, 33):
            temp = i
            a = ['0' for _ in range(6)]
            j = 0
            while temp >= 1:
                a[j] = str(temp % 2)
                j = j + 1
                temp = temp // 2
            right.append(a)
        for j in range(0, 5):
            res = []
            for i in range(0, 32):
                if int(right[i][j]) == 1:
                    res.append(i + 1)
            tmp = []
            for ite in res:
                tmp.append(ite)
            tmp_str = str(tmp) + "\n\n如果你想的数字在上面出现了，请输入 1，如果没有出现，请输入 0。\n\n请输入数字 0 或 1:  "
            a = enter_box.askinteger('info', tmp_str)
            result = pow * int(a) + result
            pow *= 2
        tmp_result = "你想的数是:" + str(result)
        box.showinfo('结果', tmp_result)
    elif Home_Choice == '计算鸡兔同笼问题':
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


        enter_head = enter_box.askinteger('输入', '头的数量')
        enter_feet = enter_box.askinteger('输入', '脚的数量')
        main(enter_head, enter_feet)
    elif Home_Choice == 'Collatz数列':
        def collatz(num):
            print('-----计算开始-----')
            print(f'初始值：{num}')
            while True:
                if num != 1:
                    if num % 2 == 0:
                        if num == 1:
                            sys.exit(7)
                        else:
                            num = num // 2
                            print(num)
                    elif num % 2 == 1:
                        if num == 1:
                            sys.exit(9)
                        else:
                            num = 3 * num + 1
                            print(num)
                else:
                    print('-----计算结束-----')
                    break


        enter_num = enter_box.askinteger('输入', """输入一个数字。程序将会以Collatz数列计算的方式计算该数字。""")
        if enter_num > 0:
            collatz(enter_num)
        else:
            box.showwarning('Collatz', 'Collatz计算方式不能计算小于/等于0的数字')
    elif Home_Choice == '激活Windows(需要管理员权限)':
        activation_choice = easygui.buttonbox('请选择激活方式', '激活Windows', ['kms网址激活', '数字权利激活'])
        if activation_choice == 'kms网址激活':
            box.showwarning('注意事项', """该功能必须在有网络时使用，且以管理员身份运行。
该功能运行时间较久，请耐心！
如跳出权限不够等相关弹窗说明没有以管理员身份运行
跳出其他弹窗纯属正常现象""")
            os.system('slmgr -skms kms.v0v.bid')
            print('已设置好kms网址...')
            os.system('slmgr -ato')
            print('激活命令结束。')
        elif activation_choice == '数字权利激活':
            box.showwarning('注意事项', """按下确定后几秒钟会弹出一个窗口。
在那个窗口中：
按下1:永久激活当前版本Windows
按下2:把Windows激活到2038年
按下3:把Windows和Office激活到180天后
(还是不会科学上网)""")
            os.system('Powershell.exe "irm https://massgrave.dev/get | iex"')
    elif Home_Choice == '九九乘法表':
        box.showinfo('info', '乘法表将会在输出区内输出')
        print('九九乘法表：')
        for i in range(1, 10):
            for j in range(1, i + 1):
                print(f'{j}x{i}={i * j}', end='\t')
            print()
    elif Home_Choice == 'BMI检测':
        bmiFile = open('H:/Projects/App/BMI/BMI Log.log', 'a')
        high = enter_box.askfloat('输入', '输入身高(m)')
        weight = enter_box.askfloat('输入', '输入体重(kg)')
        bmi = weight / (high ** 2)
        bmiFile.write(f"""\n时间:{datetime.today()}
你的身高：{high}m
你的体重：{weight}kg
BMI:{str(int(bmi))}""")
        if bmi <= 18.4:
            box.showinfo('BMI', f'你的BMI值：{bmi} 温馨提示：你的体型偏瘦，要注意营养哦~')
            bmiFile.write('\n温馨提示：你的体型偏瘦，要注意营养哦~')
        elif 18.4 < bmi <= 23.9:
            box.showinfo('BMI', f'你的BMI值：{bmi} 温馨提示：标准体型，继续保持哦~')
            bmiFile.write('\n温馨提示：标准体型，继续保持哦~')
        elif 24 <= bmi <= 27.9:
            box.showinfo('BMI', f'你的BMI值：{bmi} 温馨提示：你的体型过胖，要注意身体哦~')
            bmiFile.write('\n温馨提示：你的体型过胖，要注意身体哦~')
        elif bmi >= 28:
            box.showinfo('BMI', f'你的BMI值：{bmi} 温馨提示：你的体型肥胖，要注意饮食哦~')
            bmiFile.write('\n温馨提示：你的体型肥胖，要注意饮食哦~')
        bmiFile.write('\n---------')
        bmiFile.close()
    elif Home_Choice == '关于':
        box.showinfo('关于', version)
    elif Home_Choice is None or Home_Choice == '退出':
        end_time = time.perf_counter()
        print(f'本次运行时间:{str(end_time - start_time)}秒')
        time.sleep(end_sleep_time)
        break
