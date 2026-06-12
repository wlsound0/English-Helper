import append
import read_file as rf

def main() -> None:
    print('Made By 镜梦')
    
    check = rf.check()
    say = ('','有单词文件缺失','单词文件与统计个数文件长度不统一')
    if check == 1 or check == 2:
        inp = input(say[check]+'，是否直接初始化所有单词数据（N/Y）：')
        if inp == 'Y':
            rf.init()
        else:
            return
    elif check == 3:
        inp = input('单词文件中有重复值，是否进入选择模式（N/Y）：')
        if inp == 'Y':
            rf.choose()
        else:
            return
    file = rf.read()
    
    inp = ''
    while inp != '0':
        print('''
        选择模式：
        1.修改/显示单词本
        0.退出
        ''')
        inp = input('>>>')
        if inp == '0':
            break
        elif inp == '1':
            interrupt = append.main(file)
            if interrupt:
                break


if __name__ == '__main__':
    main()