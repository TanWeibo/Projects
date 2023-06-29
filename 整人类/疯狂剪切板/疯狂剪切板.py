from pyperclip import copy, paste

copy('剪切板已经罢工了！！！')
while True:
    try:
        now = paste()
        if now != '剪切板已经罢工了！！！':
            copy('剪切板已经罢工了！！！')
    except KeyboardInterrupt:
        print('Thanks!')
        break
