import append
import read_file as rf

def main() -> None:
    print('Made By 镜梦')
    
    if not rf.check():
        inp = input('有单词文件缺失或损坏，是否直接初始化所有单词数据（N/Y）：')
        if inp == 'Y':
            rf.init()
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
            append.show(file)


if __name__ == '__main__':
    main()