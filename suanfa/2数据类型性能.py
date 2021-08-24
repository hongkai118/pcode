# -*- coding:utf-8 -*-
"""
作者：KYLE
日期：2021年08月21日
"""

# 4种生成前n个整数列表的方法
'''
def test1():
    l=[]
    for i in range(1000):
        l=l+[i]

def test2():
    l=[]
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

from timeit import Timer
t1 = Timer("test1()","from __main__ import test1")
print("concat %f seconds \n" %t1.timeit(number=10000)) #执行1000次的时间

t2 = Timer("test2()","from __main__ import test2")
print("concat %f seconds \n" %t2.timeit(number=10000))#执行1000次的时间

t3 = Timer("test3()","from __main__ import test3")
print("concat %f seconds \n" %t3.timeit(number=10000)) #执行1000次的时间

t4 = Timer("test4()","from __main__ import test4")
print ("concat %f seconds \n" %t4.timeit(number=10000)) #执行1000次的时间
'''

#验证pop(0)和pop()的新能
#不知道为什么结果不对，因为pop()的执行时间数字太大了
import timeit
x = list(range(2000000))

popzero = timeit.Timer("x.pop(0)","from __main__ import x")
popend = timeit.Timer("x.pop()","from __main__ import x")

print(popzero.timeit(number=1000))
print(popend.timeit(number=1000))