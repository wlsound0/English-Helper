import Word
import Setting

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
    print('抽取开始，按Enter键表示下一个词，输入任意字符再按Enter表示退出')
    inp = ''
    while inp == '':
        word: Word.Word
        if mode == 1:
            word = wb.rd()
        elif mode == 2:
            word = wb.rd_use()
        print(word.word)
        inp = input()