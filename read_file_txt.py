from Class import Word
from file import read_wordbook_txt as rwt

def read() -> Word.WordBook:
    rd = rwt.read()
    words = rd[0]
    nums = rd[1]
    re: Word.WordBook = Word.WordBook()
    for i in range(len(words)):
        new_word: Word.Word = Word.Word(words[i], nums[i])
        re.push(new_word)
    return re

def write(wb: Word.WordBook):
    wt: dict[str, int] = {}
    for word in wb.words:
        wt[word.word] = word.num
    rwt.write(wt)

def choose() -> bool:
    rd: list[list] = rwt.read()
    words: list[str] = rd[0]
    nums: list[int] = rd[1]
    
    dic_words: dict[str, list[int]] = {}
    new_words: dict[str, int] = {}
    for i in range(len(words)):
        try:
            dic_words[words[i]].append(nums[i])
        except KeyError:
            dic_words[words[i]] = [nums[i]]
    
    try:
        for i in dic_words.keys():
            nms: list[int] = dic_words[i]
            if len(nms) == 1:
                new_words[i] = nms[0]
                continue
            else:
                print('\n单词：' + i)
                print('次数：', end='')
                for k in nms:
                    print(k, end=' ')
                print()
            while True:
                inp = input('重置为多少个（若填写0则表示删除）：')
                try:
                    inp = int(inp)
                except ValueError:
                    input('错误输入，按Enter后重新输入...')
                    continue
                break
            new_words[i] = inp
        rwt.write(new_words)
        return False
    except KeyboardInterrupt:
        used: list[str] = list(new_words.keys())
        rwt.write(new_words)
        for i in dic_words.keys():
            if used.count(i) == 1:
                continue
            v: list[int] = dic_words[i]
            for k in v:
                rwt.append_one(i, k)
        return True

def check() -> bool:
    '''返回是否可以继续读取文件'''
    check: int = rwt.check()
    say = ('', '有单词文件缺失', '单词文件与统计个数文件长度不统一', '', '文件格式错误')
    if check == 1 or check == 2 or check == 4:
        inp = input(say[check] + '，是否初始化所有单词数据（N/Y）：')
        if inp == 'Y':
            rwt.init()
        else:
            return False
    elif check == 3:
        inp = input('单词文件中有重复值，是否进入选择模式（N/Y）：')
        if inp == 'Y':
            interrupt= choose()
            if interrupt:
                return False
        else:
            return False
    return True
    