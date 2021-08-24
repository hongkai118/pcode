# -*- coding:utf-8 -*-
"""
作者：KYLE
日期：2021年07月17日
"""
#第1题：给定n, 计算1+2!+3!+....+n!的值
def sum_factorial(n):
    """
    #第1题：给定n, 计算1+2!+3!+....+n!的值
    :param n:
    :return: result
    """
    #第一步：

    num_li=[]
    while n>0:
        #循环一次得出一个阶乘值，放入列表
        num = 1 #初始化零时值
        for i in range(1,n+1):
            num = num*i
        num_li.append(num)
        # print(num_li)
        n = n - 1

    #统计列表里面的所有数值
    result=sum(num_li)
    print(result)

#第2题：给定y和m, 计算y年m月有几天。
    #1）注意，闰年定义。
def get_days(year, month):
    #月份字典
    dayue=[1,3,5,7,8,10,12]
    Apr=[4]
    xiaoyue=[2,6,9,11]

    # 判断是否为闰年
    if year % 100 == 0:  # 世纪年
        if year % 400 == 0:  # 400为闰年
            leapyear = True
        else:
            leapyear = False
    elif year % 4 == 0 and year % 100 != 0:
        leapyear = True
    else:
        leapyear = False

    # 如果是闰年的月份天数
    if leapyear==True:
        Apr=30
    else:
        Apr=28

    # 检车输入的月份，返回具体天数
    if month in dayue:
        result=31
    elif month in xiaoyue:
        result=30
    else:
        result=Apr

    return result

#第3题：移动字符串，例如：2)mnbol和2，返回：olmnb
def move_str(s,n):
    str_head=s[-n:]
    str_tail=s[:-n]
    new_str= str_head+str_tail
    return new_str


#第4题：给定一个英文数字字数串，打印相应的数字字符串：如 one-four-five-nine，输出1459
def string_decimal(s):
    dict_num={
        'zero':0,
        'one':1,
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9
    }

    li_s = s.split('-')
    li_num=[]
    for s_num in li_s:
        num=dict_num[s_num]
        li_num.append(str(num))
    result = ''.join(li_num)

    return result


if __name__=='__main__':
#第1题：给定n, 计算1+2!+3!+....+n!的值
# sum_factorial(10)
#第2题：给定y和m, 计算y年m月有几天。#1）注意，闰年定义。
# print(i,get_days(4001,i))

#第3题：移动字符串，例如：
#     print(move_str('abcde',3))

#第4题：给定一个英文数字字数串，打印相应的数字字符串：如 one-four-five-nine，输出1459
# print(string_decimal('one-four-nine-eight-six-five'))
    pass
