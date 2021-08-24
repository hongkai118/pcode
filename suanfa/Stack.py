# -*- coding:utf-8 -*-
"""
作者：KYLE
日期：2021年08月21日
"""
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


