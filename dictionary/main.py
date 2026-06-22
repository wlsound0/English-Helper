from pystardict import Dictionary

dic: Dictionary
loaded: bool = False

def load() -> bool:
    global dic
    global loaded
    print('正在读取字典...')
    try:
        dic = Dictionary('stardict-ecdict-2.4.2')
        loaded = True
    except FileNotFoundError:
        return False
    return True

def check() -> bool:
    return loaded

def ans(inp: str) -> None:
    global dic
    try:
        print(dic[inp])
    except KeyError:
        print('（该单词在字典中未找到）')