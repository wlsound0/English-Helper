import random

class Word:
    def __init__(self, word: str, num: int) -> None:
        self.word: str = word
        self.num: int = num
        
class WordBook:
    def __init__(self) -> None:
        self.words: list[Word] = []     # 存储Word类
        self.index: dict[str, int] = {}     # 使单词与words中的Word类的下标一一对应
        self.all_fre = 0               # 所有单词出现次数相加
        
    def push(self, word: Word) -> None:
        '''
        直接加入已有的Word类
        注：all_fre会自己更新，无需额外更新。
        '''
        self.index[word.word] = len(self.words)
        self.words.append(word)
        self.all_fre += word.num
        
    def imp(self, words: list[Word]) -> None:
        '''直接导入存有Word的列表'''
        for i in words:
            self.push(i)
            
    def find(self, word: str) -> int:
        '''查找某个单词在单词本内的位置 若不在单词本内则返回-1'''
        try:
            re = self.index[word]
        except KeyError:
            return -1
        return re
    
    def add(self, words: list[str]) -> None:
        '''
        使次数增加
        注意：参数类型是list[str]
        '''
        
        for i in words:
            ind = self.find(i)
            if ind == -1:
                new_word = Word(i, 1)
                self.push(new_word)
            else:
                self.words[ind].num += 1
                self.all_fre += 1
    
    def dec(self, words: list[str]) -> list[str]:
        '''
        使次数减少，返回值为所有错误输入
        注意：参数类型是list[str]
        '''
        
        re: list[str] = []
        for i in words:
            ind = self.find(i)
            if ind == -1:
                re.append(i)
            else:
                self.words[ind].num -= 1
                if self.words[ind].num == 0:
                    del self.words[ind]
                    del self.index[i]
                    for k in self.index.keys():
                        if self.index[k] > ind:
                            self.index[k] -= 1
                self.all_fre -= 1
        return re
    
    def to_dict(self) -> dict[str, int]:
        re: dict[str, int] = {}
        for i in self.words:
            re[i.word] = i.num
        return re
    
    def rd(self) -> Word:
        '''纯随机产生一个单词 注意：使用前确保单词本不为空'''
        index = random.randint(0, len(self.words) - 1)
        return self.words[index]
    
    def rd_use(self) -> Word:
        '''根据出现次数调整权重地产生单词'''
        rt = random.randint(1, self.all_fre)
        index = -1
        while rt > 0:
            index += 1
            rt -= self.words[index].num
        return self.words[index]
    
    def query(self, what: str) -> int:
        '''查询该单词在单词本中记录了几次'''
        try:
            return self.words[self.index[what]].num
        except KeyError:
            return 0
    