from pystardict import Dictionary
import os

dic: Dictionary
loaded: bool = False

def load() -> bool:
    global dic
    global loaded
    print('正在读取字典...')
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        dict_path = os.path.join(script_dir, 'stardict-ecdict-2.4.2')
        dic = Dictionary(dict_path)
        loaded = True
    except FileNotFoundError:
        return False
    return True

def check() -> bool:
    return loaded

def ans(inp: str) -> None:
    global dic
    re = dic[inp]
    if re:
        print(re)
    else:
        print('（该单词/词组不在词典中）')
        
if __name__ == '__main__':
    load()
    ans('hello')
    ans('world')
    ans('apple')
    ans('aaaaappplee')