def init() -> None:
    with open('words.txt', 'w'):
        pass
    with open('nums.txt', 'w'):
        pass
    
def check() -> bool:
    # 检查文件完整性
    try:
        words_len = 0
        nums_len = 0
        with open('words.txt', 'r') as f:
            for i in f:
                words_len += 1
        with open('nums.txt', 'r') as f:
            for i in f:
                nums_len += 1
        if words_len != nums_len:
            return False
    except FileNotFoundError:
        return False
    return True

def read() -> dict:
    # 读取
    words = []
    with open('words.txt', 'r') as f:
        for word in f:
            words.append(word.strip())
    nums = []
    with open('nums.txt', 'r') as f:
        for num in f:
            nums.append(int(num.strip()))
    re = {}
    for i in range(len(words)):
        re[words[i]] = nums[i]
    return re
        
def write(new: dict) -> None:
    # 写入
    words = ''
    nums = ''
    for i in new.keys():
        words += i
        words += '\n'
        nums += str(new[i])
        nums += '\n'
    with open('words.txt', 'w') as f:
        f.write(words)
    with open('nums.txt', 'w') as f:
        f.write(nums)