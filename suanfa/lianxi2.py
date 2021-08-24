# -*- coding:utf-8 -*-
"""
作者：KYLE
日期：2021年07月18日
"""
#第一题：水仙花数，如果这个数为m位数，则每个位上的m次幂之后等于它本身。
#例如：1^3+5^3+3^3=153, 1^4+6^4+3^4+4^4=1634
def sxh(num):
    # 判断有几位
    s_num = str(num)  #
    num_lens = len(s_num)

    # 取得每一个上的数字
    # 1. 取得数字符串的数字
    # 2. 将数字加到列表中
    temp_num_li = []
    for i in s_num:
        num_i = int(i)
        temp_num = num_i ** (num_lens)
        temp_num_li.append(temp_num)

    # 3. 计算列表的值
    result = sum(temp_num_li)

    if result == num:
        return True
    else:
        return False

#2. 求字符串并集
def binji(s1,s2):
    set1=set(s1)
    set2=set(s2)
    new_set=set1&set2
    print(new_set)


if __name__=='__main__':
    #1求水仙花
    # for i in range(100,1000):
    #     if sxh(i):
    #         print('水仙花数:',i)

#2字符串的并集
    # binji('abcda','aabc')

    help(binji)




