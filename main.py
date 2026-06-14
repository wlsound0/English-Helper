import append
import read_file as rf
import Word
import draw_word
import Setting

def main() -> None:
    print('Made By 镜梦')
    interrupt = False
    
    check: int = rf.check()
    say = ('', '有单词文件缺失', '单词文件与统计个数文件长度不统一', '', '文件格式错误')
    if check == 1 or check == 2 or check == 4:
        inp = input(say[check] + '，是否初始化所有单词数据（N/Y）：')
        if inp == 'Y':
            rf.init()
        else:
            return
    elif check == 3:
        inp = input('单词文件中有重复值，是否进入选择模式（N/Y）：')
        if inp == 'Y':
            interrupt= rf.choose()
            if interrupt:
                return
        else:
            return
    wb: Word.WordBook = rf.read()
    
    check = Setting.check()
    say = ('', '设置文件缺失', '设置文件格式错误', '')
    if check == 1 or check == 2:
        inp = input(say[check] + '，是否初始化所有设置数据（N/Y）：')
        if inp == 'Y':
            Setting.init()
        else:
            return
    elif check == 3:
        inp = input('设置文件有参数缺失，是否进入设置模式（N/Y）：')
        if inp == 'Y':
            interrupt = Setting.choose()
            if interrupt:
                return
        else:
            return
    st: Setting.Settings = Setting.load()
    
    inp = ''
    while inp != '0':
        print('''
        选择模式：
        1. 修改/显示单词本
        2. 抽取单词
        3. 设置
        0. 退出
        ''')
        inp = input('>>>')
        if inp == '0':
            break
        elif inp == '1':
            interrupt = append.main(wb)
            if interrupt:
                break
        elif inp == '2':
            if wb.all_fre == 0:
                print('当前还没有任何单词哦，请添加后重试')
                input('按Enter后重新输入...')
            else:
                draw_word.main(wb, st)
        elif inp == '3':
            interrupt = Setting.main(st)
            if interrupt:
                break
        else:
            input('错误输入，按Enter后重新输入...')

if __name__ == '__main__':
    main()