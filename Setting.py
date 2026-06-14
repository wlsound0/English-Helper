import json


re_name = ('单词本储存格式', '抽取模式')
re_choose = (
    ('文本文档模式', ), 
    ('纯随机模式', '按出现次数智能随机', '每次进入抽取模式时确认')
)
re_result = (
    ('txt', 'SQL'), 
    ('random', 'times', 'sure')
)
mode_name = (
    'file_mode', 
    'draw_mode'
)
setting_print = (
    {
        'txt': '文本文档格式', 
        'SQL': 'SQL格式'
    }, 
    {
        'random': '纯随机模式', 
        'times': '按出现次数智能随机', 
        'sure': '每次进入抽取模式时确认'
    }
)

class Settings:
    file_mode: str
    draw_mode: str
    def __init__(self, file_mode, draw_mode) -> None:
        self.file_mode = file_mode
        self.draw_mode = draw_mode
    def to_dict(self) -> dict:
        re: dict = {}
        re['file_mode'] = self.file_mode
        re['draw_mode'] = self.draw_mode
        return re
    def dict_to(self, d: dict) -> None:
        self.file_mode = d['file_mode']
        self.draw_mode = d['draw_mode']
    def change(self, mode: str, what: str) -> None:
        d: dict = self.to_dict()
        d[mode] = what
        self.dict_to(d)
        

def check() -> int:
    '''
    1. 文件缺失
    2. 格式错误
    3. 参数缺失
    0. 正常
    '''
    try:
        with open('settings.json', 'r') as f:
            data = json.load(f)
        name = ('file_mode', 'draw_mode')
        for k in range(len(name)):
            a = data[name[k]]
    except FileNotFoundError:
        return 1
    except json.JSONDecodeError:
        return 2
    except KeyError:
        return 3
    return 0        
    
def write_dict(data: dict) -> None:
    with open('settings.json', 'w') as f:
        json.dump(data, f)
    
def choose() -> bool:
    miss = []
    new_data: dict = {}
    with open('settings.json', 'r') as f:
        data = json.load(f)
    name = ('file_mode', 'draw_mode')
    for i in range(len(name)):
        try:
            new_data[name[i]] = data[name[i]]
        except KeyError:
            miss.append(i)
    
    for i in miss:
        while True:
            print(re_name[i] + '：')
            for k in range(len(re_choose[i])):
                print(str(k+1) + '. ' + re_choose[i][k])
            try:
                inp = input('>>>')
            except KeyboardInterrupt:
                write_dict(new_data)
                return True
            try:
                inp = int(inp)
                if inp > 0 and inp <= len(re_choose[i]):
                    break
                input('错误输入，请重新输入...')
            except ValueError:
                input('错误输入，请重新输入...')
        inp = inp - 1
        new_data[mode_name[i]] = re_result[i][inp]
    write_dict(new_data)
    return False
    
def load() -> Settings:
    with open('settings.json', 'r') as f:
        settings = json.load(f)
    re: Settings = Settings(settings['file_mode'], settings['draw_mode'])
    return re

def write(s: Settings) -> None:
    data: dict = {}
    data['file_mode'] = s.file_mode
    data['draw_mode'] = s.draw_mode
    write_dict(data)

def init() -> None:
    new = Settings('txt', 'sure')
    write(new)
    

def main(settings: Settings) -> bool:
    try:
        inp = ''
        while inp != 'Exit':
            d: dict = settings.to_dict()
            while True:
                print()
                print('        设置（输入Exit退出）：')
                for i in range(len(re_choose)):
                    print('        ' + str(i + 1) + '. ' + re_name[i] + '：' + setting_print[i][d[mode_name[i]]])
                inp = input('>>>')
                if inp == 'Exit':
                    break
                try:
                    inp = int(inp)
                    if inp > 0 and inp <= len(re_choose):
                        break
                    input('错误输入，按Enter后重新输入...')
                except ValueError:
                    input('错误输入，按Enter后重新输入...')
            if inp == 'Exit':
                break
            print()
            inp = inp - 1
            inpp = ''
            while True:
                print('        ' + re_name[inp] + '：')
                for i in range(len(re_result[inp])):
                    print('        ' + str(i + 1) + '. ' + setting_print[inp][re_result[inp][i]])
                inpp = input('>>>')
                try:
                    inpp = int(inpp)
                    if inpp > 0 and inpp <= len(re_result[inp]):
                        break
                    input('错误输入，按Enter后重新输入...')
                except ValueError:
                    input('错误输入，按Enter后重新输入...')
            settings.change(mode_name[inp], re_result[inp][inpp - 1])
    except KeyboardInterrupt:
        write(settings)
        return True
    write(settings)
    return False

if __name__ == '__main__':
    setting = load()
    main(setting)