#命令行常用输入输出方式
#import msvcrt
#ch = msvcrt.getch().decode(encoding='utf-8') #只能返回一个字符,就自动执行下一行代码，且不显示输入内容
#msvcrt.putch('*'.encode(encoding='utf-8')) #输出'*'星号。
#笔记：因此可以用while语言，输入字符，输入一次就是现实一个星号。

#**********************示例代码密码星号输出***************************

import msvcrt
def pwd_input(text):
    """
    输入信息加密
    """
    print(text,end='',flush=True)
    chars = []
    while True:
        try:
            newChar = msvcrt.getch().decode(encoding="utf-8")
        except:
            return input("你很可能不是在cmd命令行下运行，密码输入将不能隐藏:")
        # 换行 -- 输入结束
        if newChar in '\r\n': 
             break
        # 如果是退格，则删除密码末尾一位并且删除一个星号
        elif newChar == '\b': # 如果是退格，则删除密码末尾一位并且删除一个星号
             if chars:
                 del chars[-1]
                 # 光标回退一格
                 msvcrt.putch('\b'.encode(encoding='utf-8')) 
                 # 输出一个空格覆盖原来的星号
                 msvcrt.putch( ' '.encode(encoding='utf-8')) 
                 # 光标回退一格准备接受新的输入
                 msvcrt.putch('\b'.encode(encoding='utf-8')) 
        else:
            chars.append(newChar)
            # 命令行中显示为星号
            msvcrt.putch('*'.encode(encoding='utf-8')) 
    # 返回真实信息
    return (''.join(chars))

if __name__=='__main__':
    pwd=pwd_input('输入密码：')
    print('\n密码是：',pwd)