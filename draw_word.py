from Class import Word
from Class import Setting
import random
from dictionary import main as dic

def ch_mode() -> int:
    while True:
        print('''
        请选择模式：
        1. 纯随机抽取
        2. 根据单词出现次数调整权重抽取
        0. 退出
        ''')
        inp = input('>>>')
        try:
            inp = int(inp)
            if inp < 0 or inp > 2:
                input('错误输入，按Enter后重新输入...')
                continue
            break
        except ValueError:
            input('错误输入，按Enter后重新输入...')
    return inp

def ch_dic() -> int:
    while True:
        print('''
        是否启用字典？：
        1. 是
        2. 否
        0. 退出
        ''')
        inp = input('>>>')
        try:
            inp = int(inp)
            if inp < 0 or inp > 2:
                input('错误输入，按Enter后重新输入...')
                continue
            break
        except ValueError:
            input('错误输入，按Enter后重新输入...')
    return inp

def main(wb: Word.WordBook, st: Setting.Settings) -> None:
    mode = -1
    if st.draw_mode == 'sure':
        mode = ch_mode()
        if mode == 0:
            return
    else:
        d: dict = {
            'random': 1, 
            'times': 2
        }
        mode = d[st.draw_mode]
    
    use_dict: int
    if st.use_dict == 'sure':
        use_dict = ch_dic()
        if use_dict == 0:
            return
    else:
        d: dict = {
            'true': 1, 
            'false': 2
        }
        use_dict = d[st.use_dict]
    if use_dict == 1 and not dic.check():
        can_load = dic.load()
        if not can_load:
            print('读取字典失败，请检查字典文件是否存在！！！')
            input('按Enter返回主界面...')
            return
        
    print('抽取开始，按Enter键表示下一个词，输入任意字符再按Enter表示退出')
    inp = ''
    while inp == '':
        word: Word.Word
        if mode == 1:
            word = wb.rd()
        elif mode == 2:
            word = wb.rd_use()
        print(word.word)
        if use_dict == 1:
            inp = input()
            if inp == '':
                dic.ans(word.word)
            else:
                break
        inp = input()