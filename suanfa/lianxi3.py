# -*- coding:utf-8 -*-
"""
作者：KYLE
日期：2021年07月25日
"""

import time

#计算n的阶乘累加需要的时间
def jiecheng(n):
    num_li=[]
    while n>0:
        num=1
        for i in range(1,n+1):
            num=num*i

        num_li.append(num)
        n=n-1
    result = sum(num_li)
    return result

def time_cost_jiecheng():

    # for i in (100,1000,10000):
    for i in range(1000,1100):
        time1=time.time()
        result=jiecheng(i)
        time2=time.time()
        cost_time=time2-time1

        print(i,cost_time)






if __name__=='__main__':
    time_cost_jiecheng()