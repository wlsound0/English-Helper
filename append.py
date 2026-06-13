import read_file as rf
import Word
interrupt = False

def check(word: str) -> bool:
    if len(word) == 0 or word[0] == ' ':
        return True
    return False

def re_all(wb: Word.WordBook) -> None:
    # 返回所有单词
    words: dict = wb.to_dict()
    for word, num in sorted(words.items(), key=lambda item: item[1], reverse=True):
        print('        ' + word + ': ' + str(num))

def re_some(wb: Word.WordBook, x: int) -> None:
    # 返回频率为前x的单词
    i = 0
    words: dict = wb.to_dict()
    for word, num in sorted(words.items(), key=lambda item: item[1], reverse=True):
        i += 1
        print(str(word) + ': ' + str(num))
        if i == x:
            return

def show(wb: Word.WordBook) -> None:
    print('###################################\n')
    re_all(wb)
    print('\n输入Exit退出，输入+++进入批量添加模式，输入---进入批量减少模式。')
    print('输入其他单词表示某单词数量+1，若需要某单词数量-1则在单词前输入减号。')
    
def multyap(wb: Word.WordBook) -> Word.WordBook:
    # 批量添加
    inp = ''
    try:
        while inp != 'Exit':
            show(wb)
            print('已进入批量添加模式。该模式下，一行可以添加多个单词，每个单词之间用英文逗号分隔，不要加空格。')
            inp = input('>>>')
            if check(inp):
                input('错误输入，按Enter键后重新输入')
                continue
            if inp == 'Exit':
                break
            word = ''
            words: list[str] = []
            for i in inp:
                if i == ',':
                    if not check(word):
                        words.append(word)
                    word = ''
                else:
                    word += i
            if inp[-1] != ',' and not check(word):
                words.append(word)
            wb.add(words)
    except KeyboardInterrupt:
        global interrupt
        interrupt = True
        return wb
    return wb
            
def multydl(wb: Word.WordBook) -> Word.WordBook:
    # 批量减少
    inp = ''
    try:
        while inp != 'Exit':
            show(wb)
            print('已进入批量减少模式。该模式下，一行可以减少多个单词，每个单词之间用英文逗号分隔，不要加空格。')
            inp = input('>>>')
            if check(inp):
                input('错误输入，按Enter键后重新输入')
                continue
            if inp == 'Exit':
                break
            word = ''
            words: list[str] = []
            for i in inp:
                if i == ',':
                    if not check(word):
                        words.append(word)
                    word = ''
                else:
                    word += i
            if inp[-1] != ',' and not check(word):
                words.append(word)
            wrong: list[str] = wb.dec(words)
            if len(wrong) != 0:
                print('提醒：下述单词原本就不存在于单词本中，所以无法减小：')
                for i in range(len(wrong)):
                    if i == len(wrong) - 1:
                        print(wrong[i])
                    else:
                        print(wrong[i], end=',')
                input('其余单词已成功减小，按Enter键以继续...')
    except KeyboardInterrupt:
        global interrupt
        interrupt = True
        return wb
    return wb

def main(wb: Word.WordBook) -> bool:
    global interrupt
    inp = ''
    try:
        while inp != 'Exit':
            show(wb)
            inp = input('>>>')
            if check(inp):
                input('错误输入，按Enter键后重新输入...')
                continue
            if inp == 'Exit':
                # 退出
                break
            if inp == '+++':
                wb = multyap(wb)
            elif inp == '---':
                wb = multydl(wb)
            elif inp[0] != '-':
                wb.add([inp])
            else:
                word = inp[1:]
                if check(word):
                    input('错误输入，按Enter键后重新输入...')
                    continue
                wb.dec([word])
            if interrupt:
                rf.write(wb.to_dict())
                return True
    except KeyboardInterrupt:
        rf.write(wb.to_dict())
        return True
    rf.write(wb.to_dict())
    return False