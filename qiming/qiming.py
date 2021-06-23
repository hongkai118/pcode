import random
import re


def get_name(last_name,num):

    with open('F:\\pcode\\qiming\\xing.txt') as xf:
        xing=xf.read()

    with open('F:\\pcode\\qiming\\ming.txt') as mf:
        ming=mf.read()

    #去掉换行符
    xing=xing.replace('\n','')
    ming=ming.replace('\n','')
    ming=ming.replace(' ','')
    ming=ming.replace('，','')
    ming=ming.replace('；','')

    if last_name=='':
        for i in range(20):
            x_name = random.choice(xing)
            m_temp = random.sample(ming,num)
            m_name=''.join(m_temp)
            
            name = x_name+m_name
            print(name)
        
    else:
        for i in range(20):
            x_name=last_name
            m_temp = random.sample(ming,num)
            m_name=''.join(m_temp)
            m_name=m_name.strip()
            
            name = x_name+m_name
            print(name)
    
if __name__=='__main__':
    # num=input('名字位数：')
    # num=int(num)
    # num=num-1

    # xing=input('输入姓：',)

    print('结果为如下：')

    #num=1是表示2字姓名，num=2是3字姓名
    get_name(last_name='',num=2)






    