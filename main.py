import append
import read_file_txt as rft
from Class import Word
import draw_word
import setting
from Class import Setting

def main() -> None:
    print('Made By 镜梦')
    interrupt = False
    
    con = rft.check()
    if not con:
        return
    wb: Word.WordBook = rft.read()
    
    con = setting.check()
    if not con:
        return
    st: Setting.Settings = setting.read()
    
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
            interrupt = setting.main(st)
            if interrupt:
                break
        else:
            input('错误输入，按Enter后重新输入...')

if __name__ == '__main__':
    main()