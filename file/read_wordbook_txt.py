from .storage import Txt

def init() -> None:
    Txt.write('words.txt', '')
    Txt.write('nums.txt', '')
    
def read() -> list:
    # 读取
    words: list[str] = []
    with open('words.txt', 'r') as f:
        for word in f:
            words.append(word.strip())
    nums: list[int]  = []
    with open('nums.txt', 'r') as f:
        for num in f:
            nums.append(int(num.strip()))
    return [words, nums]


def write(new: dict[str, int]) -> None:
    # 写入
    words = ''
    nums = ''
    for i in new.keys():
        words += i
        words += '\n'
        nums += str(new[i])
        nums += '\n'
    Txt.write('words.txt', words)
    Txt.write('nums.txt', nums)

def append(new: dict[str, int]) -> None:
    # 追加
    words = ''
    nums = ''
    for i in new.keys():
        words += i
        words += '\n'
        nums += str(new[i])
        nums += '\n'
    Txt.append('words.txt', words)
    Txt.append('nums.txt', nums)

def append_one(new_word: str, new_nums: int):
    Txt.append('words.txt', new_word + '\n')
    Txt.append('nums.txt', str(new_nums) + '\n')

def check() -> int:
    # 检查文件完整性
    """
    0 无错误
    1 文件缺失
    2 单词与统计个数长度不统一
    3 有重复单词
    4 文件格式错误
    """
    try:
        rd = read()
        words: list[str] = rd[0]
        nums: list[int] = rd[1]
        if len(words) != len(nums):
            return 2
        if len(words) != len(set(words)):
            return 3
    except ValueError:
        return 4
    except FileNotFoundError:
        return 1
    return 0

