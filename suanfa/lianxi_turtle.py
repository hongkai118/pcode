# -*- coding:utf-8 -*-
"""
作者：KYLE
日期：2021年07月25日
"""

# #画一个三角形
# import turtle #导入turtle模块
# p=turtle.Pen() #创建一支画笔（海龟）
# p.pencolor('blue') #设置画笔为蓝色
# p.pensize(5) #画笔粗细为5
# p.forward(100) #最初画笔（海龟）朝向正右方，向前画长度100的直线
# p.left(120) #左转120度
# p.forward(100) #向前运动100
# p.left(120) #左转120度
# p.forward(100) #向前运动120
# p.left(120) #左转120，变为初始方向
# turtle.done() #保持画图窗口不退出

# #画五角星
# import turtle
# t= turtle.Pen()
# # w= turtle.Screen()
# for i in range(5):
#     t.forward(100)
#     t.right(144)
# turtle.done()

import turtle

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen) #画主干
        t.right(20) #右转20度
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)
    # if branchLen <=5:
    #     t.forward(10)
    #     # t.pensize()
    #     t.pencolor('green')


if __name__=='__main__':
    t= turtle.Turtle() #生成海龟
    myWin=turtle.Screen()
    t.left(90) #海龟朝向正北
    t.up() #抬起海龟
    t.backward(200) #回退200具体
    t.down() #放下海龟
    t.color('brown') #设置颜色
    tree(80,t) #条用话术的颜色

    turtle.done()


#画一个正方形
import turtle
# t = turtle.Pen()
# t.color('green')
# t.pensize(5)
# for i in range(4):
#     t.forward(100)
#     t.right(90)
# turtle.done()

#五角星
# import turtle
# t=turtle.Pen()
# t.pencolor('red')
# t.pensize(7)
# for i in range(5):
#     t.forward(100)
#     t.right(144)
# turtle.done()

#二叉树

