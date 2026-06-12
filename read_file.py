def init() -> None:
    with open('words.txt', 'w'):
        pass
    with open('nums.txt', 'w'):
        pass
    
def check() -> int:
    # 检查文件完整性
    """
    0 无错误
    1 文件缺失
    2 单词与统计个数长度不统一
    3 有重复单词
    """
    try:
        words = []
        nums = []
        with open('words.txt', 'r') as f:
            for i in f:
                words.append(i.strip())
                
        with open('nums.txt', 'r') as f:
            for i in f:
                nums.append(i.strip())
        
        if len(words) != len(nums):
            return 2
        for i in words:
            if words.count(i) != 1:
                return 3
    except FileNotFoundError:
        return 1
    return 0

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
        
def choose() -> None:
    words = []
    nums = []
    with open('words.txt', 'r') as f:
        for i in f:
            words.append(i.strip())
    with open('nums.txt', 'r') as f:
        for i in f:
            nums.append(i.strip())
    dic_words = {}
    new_words = {}
    for i in range(len(words)):
        try:
            dic_words[words[i]].append(nums[i])
        except KeyError:
            dic_words[words[i]] = [nums[i]]
    
    try:
        for i in dic_words.keys():
            nms = dic_words[i]
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
        write(new_words)
    except KeyboardInterrupt:
        used = list(new_words.keys())
        write(new_words)
        old_words = []
        old_nums = []
        for i in dic_words.keys():
            if used.count(i) == 1:
                continue
            v = dic_words[i]
            for k in v:
                old_words.append(i)
                old_nums.append(k)
        with open('words.txt', 'a') as f:
            for i in old_words:
                f.write(i + '\n')
        with open('nums.txt', 'a') as f:
            for i in old_nums:
                f.write(i + '\n')