import read_file as rf

def check(word: str) -> bool:
    if len(word) == 0 or word[0] == ' ':
        return True
    return False

def re_all(file: dict) -> None:
    # 返回所有单词
    for word, num in sorted(file.items(), key=lambda item: item[1], reverse=True):
        print(str(word) + ': ' + str(num))

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
        input('输入错误，按任意键后重新输入...')
    return file

def show(file: dict) -> None:
    inp = ''
    while inp != 'Exit':
        print('###################################')
        re_all(file)
        print('输入Exit退出，输入其他单词表示某单词数量+1，若需要某单词数量-1则在单词前输入减号。')
        inp = input('>>>')
        if inp == 'Exit':
            break
        if check(inp):
            input('输入错误，按任意键后重新输入...')
            continue
        if inp[0] != '-':
            file = ap(file, inp)
        else:
            word = inp[1:]
            if check(word):
                input('输入错误，按任意键后重新输入...')
                continue
            file = dl(file, word)
    rf.write(file)
    return