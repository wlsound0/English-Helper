from pystardict import Dictionary

print('正在读取字典...')
dic = Dictionary('stardict-ecdict-2.4.2')

def check(inp: str):
    print(dic[inp])