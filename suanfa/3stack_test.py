# -*- coding:utf-8 -*-
"""
作者：KYLE
日期：2021年08月21日
"""

# 目录栈的应用
# 1.1 简单括号匹配
# 1.2 扩展括号匹配
# 2.1 十进制转换为二进制

# 测试栈是否可用。
# from Stack import Stack
# s=Stack()
#
# print(s.isEmpty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.isEmpty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())

from Stack import Stack


# 栈的应用1：简单括号匹配
def parChecker(symbolString):
    s = Stack()
    balance = True
    index = 0

    while index < len(symbolString) and balance:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balance = False
            else:
                s.pop()
        index = index + 1

    if balance and s.isEmpty():  # 如果不设置s.isEmpty,如果全是左括号，则balance就是True
        return True
    else:
        return False


# 栈的应用1.5:简单括号匹配
def parChecker(symbolString):
    s = Stack()
    pos = 0
    result = True
    while pos < len(symbolString) and result:
        symbol = symbolString[pos]

        if symbol in '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                result = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    result = False
        pos = pos + 1

    if result and s.isEmpty():
        return True
    else:
        return False


def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


# print(parChecker('{[(()))(]}'))
# print(parChecker('{[((()))]}'))
# print(parChecker('([])'))


# 栈的应用2：十进制转换为二进制
def divideBy2(decNumber):
    s = Stack()

    while decNumber > 0:
        rem = decNumber % 2  # 求余数
        s.push(rem)
        decNumber = decNumber // 2  # 整除2，不返回余数

    binString = ''
    while not s.isEmpty():
        binString = binString + str(s.pop())
    return binString

# print(divideBy2(3))


# 栈的应用2.1：16进制以内任意进制的转化
def baseConverter(decNumber, base):
    s = Stack()
    digits = "0123456789ABCDEF"

    while decNumber > 0:
        rem = decNumber % base
        s.push(rem)
        decNumber = decNumber // base

    baseString = ''
    while not s.isEmpty():
        baseString = baseString + digits[s.pop()]
    return baseString

print(baseConverter(1024,16))
print(baseConverter(1024,2))
