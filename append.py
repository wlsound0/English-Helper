import read_file as rf
interrupt = False

def check(word: str) -> bool:
    if len(word) == 0 or word[0] == ' ':
        return True
    return False

def re_all(file: dict) -> None:
    # 返回所有单词
    for word, num in sorted(file.items(), key=lambda item: item[1], reverse=True):
        print('        ' + word + ': ' + str(num))

def re_some(file: dict, x: int) -> None:
    # 返回频率为前x的单词
    i = 0
    for word, num in sorted(file.items(), key=lambda item: item[1], reverse=True):
        i += 1
        print(str(word) + ': ' + str(num))
        if i == x:
            return
        
def ap(file: dict, word: str) -> dict:
    # 某单词次数+1
    try:
        file[word] += 1
    except KeyError:
        file[word] = 1
    return file

def dl(file: dict, word: str) -> dict:
    try:
        file[word] -= 1
        if file[word] == 0:
            del file[word]
    except KeyError:
        input('错误输入，按Enter键后重新输入...')
    return file

def show(file: dict) -> None:
    print('###################################\n')
    re_all(file)
    print('\n输入Exit退出，输入+++进入批量添加模式，输入---进入批量减少模式。')
    print('输入其他单词表示某单词数量+1，若需要某单词数量-1则在单词前输入减号。')
    
def multyap(file: dict) -> dict:
    # 批量添加
    inp = ''
    try:
        while inp != 'Exit':
            show(file)
            print('已进入批量添加模式。该模式下，一行可以添加多个单词，每个单词之间用英文逗号分隔，不要加空格。')
            inp = input('>>>')
            if check(inp):
                input('错误输入，按Enter键后重新输入')
                continue
            if inp == 'Exit':
                break
            word = ''
            for i in inp:
                if i == ',':
                    if not check(word):
                        file = ap(file, word)
                    word = ''
                else:
                    word += i
            if inp[-1] != ',' and not check(word):
                file = ap(file, word)
    except KeyboardInterrupt:
        global interrupt
        interrupt = True
        return file
    return file
            
def multydl(file: dict) -> dict:
    # 批量减少
    inp = ''
    try:
        while inp != 'Exit':
            show(file)
            print('已进入批量减少模式。该模式下，一行可以减少多个单词，每个单词之间用英文逗号分隔，不要加空格。')
            print('注：本模式下，若输入了不存在原单词本的单词，就会触发错误提示。但请放心，所有正常的单词输入都会执行，而所有不正常的单词输入都不会执行。')
            inp = input('>>>')
            if check(inp):
                input('错误输入，按Enter键后重新输入')
                continue
            if inp == 'Exit':
                break
            word = ''
            for i in inp:
                if i == ',':
                    file = dl(file, word)
                    word = ''
                else:
                    word += i
            if inp[-1] != ',':
                file = dl(file, word)
    except KeyboardInterrupt:
        global interrupt
        interrupt = True
        return file
    return file

def main(file: dict) -> bool:
    global interrupt
    inp = ''
    try:
        while inp != 'Exit':
            show(file)
            inp = input('>>>')
            if check(inp):
                input('错误输入，按Enter键后重新输入...')
                continue
            if inp == 'Exit':
                # 退出
                break
            if inp == '+++':
                file = multyap(file)
            elif inp == '---':
                file = multydl(file)
            elif inp[0] != '-':
                file = ap(file, inp)
            else:
                word = inp[1:]
                if check(word):
                    input('错误输入，按Enter键后重新输入...')
                    continue
                file = dl(file, word)
            if interrupt:
                rf.write(file)
                return True
    except KeyboardInterrupt:
        rf.write(file)
        return True
    rf.write(file)
    return False