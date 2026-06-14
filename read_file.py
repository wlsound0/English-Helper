import Word

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
    4 文件格式错误
    """
    try:
        words: list[str] = []
        nums: list[str] = []
        with open('words.txt', 'r') as f:
            for i in f:
                words.append(i.strip())
                
        with open('nums.txt', 'r') as f:
            for i in f:
                nums.append(i.strip())
                
        if len(words) != len(nums):
            return 2
        if len(words) != len(set(words)):
            return 3
        for i in nums:
            try:
                a = int(i)
            except ValueError:
                return 4
    except FileNotFoundError:
        return 1
    return 0

def read() -> Word.WordBook:
    # 读取
    words: list[str] = []
    with open('words.txt', 'r') as f:
        for word in f:
            words.append(word.strip())
    nums: list[int]  = []
    with open('nums.txt', 'r') as f:
        for num in f:
            nums.append(int(num.strip()))
    re: Word.WordBook = Word.WordBook()
    for i in range(len(words)):
        new_word: Word.Word = Word.Word(words[i], nums[i])
        re.push(new_word)
    return re
        
def write(new: dict[str, int]) -> None:
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
        
def choose() -> bool:
    words: list[str] = []
    nums: list[int] = []
    with open('words.txt', 'r') as f:
        for i in f:
            words.append(i.strip())
    with open('nums.txt', 'r') as f:
        for i in f:
            nums.append(int(i.strip()))
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
        write(new_words)
        return False
    except KeyboardInterrupt:
        used: list[str] = list(new_words.keys())
        write(new_words)
        old_words: list[str] = []
        old_nums: list[int] = []
        for i in dic_words.keys():
            if used.count(i) == 1:
                continue
            v: list[int] = dic_words[i]
            for k in v:
                old_words.append(i)
                old_nums.append(k)
        with open('words.txt', 'a') as f:
            for i in old_words:
                f.write(i + '\n')
        with open('nums.txt', 'a') as f:
            for i in old_nums:
                f.write(str(i) + '\n')
        return True