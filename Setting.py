from Class import Setting
from file import read_setting as rs
from Class import SettingOption as ST

def keys(d: dict) -> list[str]:
    re: list[str] = []
    for i in d.keys():
        re.append(i)
    return re

st = [
    ST.SettingOption(
        'file_mode', '单词文本存储格式', {
            'txt': '文本文档格式', 
            'SQL': 'SQL格式'
        }
    ), 
    ST.SettingOption(
        'draw_mode', '抽取模式', {
            'random': '纯随机模式', 
            'times': '按出现次数智能随机', 
            'sure': '每次进入抽取模式时询问', 
        }
    ), 
]

def read() -> Setting.Settings:
    rd = rs.read()
    re = Setting.Settings()
    for i in rd.keys():
        re.change(i, rd[i])
    return re

def choose() -> bool:
    miss = []
    new_data: dict = {}
    data = rs.read()
    for i in range(len(st)):
        try:
            new_data[st[i].key] = data[st[i].key]
        except KeyError:
            miss.append(i)
    
    for i in miss:
        while True:
            print(st[i].name + '：')
            for k in range(len(st[i].choises)):
                print(str(k+1) + '. ' + keys(st[i].choises)[k])
            try:
                inp = input('>>>')
            except KeyboardInterrupt:
                rs.write(new_data)
                return True
            try:
                inp = int(inp)
                if inp > 0 and inp <= len(st[i].choises):
                    break
                input('错误输入，请重新输入...')
            except ValueError:
                input('错误输入，请重新输入...')
        inp = inp - 1
        new_data[st[i].key] = keys(st[i].choises)[inp]
    rs.write(new_data)
    return False
    
def main(settings: Setting.Settings) -> bool:
    try:
        inp = ''
        while inp != 'Exit':
            d: dict = settings.to_dict()
            while True:
                print()
                print('        设置（输入Exit退出）：')
                for i in range(len(st)):
                    print('        ' + str(i + 1) + '. ' + st[i].name + '：' + st[i].choises[d[st[i].key]])
                inp = input('>>>')
                if inp == 'Exit':
                    break
                try:
                    inp = int(inp)
                    if inp > 0 and inp <= len(st):
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
                print('        ' + st[inp].name + '：')
                for i in range(len(st[inp].choises)):
                    print('        ' + str(i + 1) + '. ' + st[inp].choises[keys(st[inp].choises)[i]])
                inpp = input('>>>')
                try:
                    inpp = int(inpp)
                    if inpp > 0 and inpp <= len(st[inp].choises):
                        break
                    input('错误输入，按Enter后重新输入...')
                except ValueError:
                    input('错误输入，按Enter后重新输入...')
            settings.change(st[inp].key, keys(st[inp].choises)[inpp - 1])
    except KeyboardInterrupt:
        rs.write(settings.to_dict())
        return True
    rs.write(settings.to_dict())
    return False

def check() -> bool:
    check = rs.check()
    say = ('', '设置文件缺失', '设置文件格式错误', '')
    if check == 1 or check == 2:
        inp = input(say[check] + '，是否初始化所有设置数据（N/Y）：')
        if inp == 'Y':
            rs.init()
        else:
            return False
    elif check == 3:
        inp = input('设置文件有参数缺失，是否进入设置模式（N/Y）：')
        if inp == 'Y':
            interrupt = choose()
            if interrupt:
                return False
        else:
            return False
    return True

if __name__ == '__main__':
    setting = read()
    main(setting)