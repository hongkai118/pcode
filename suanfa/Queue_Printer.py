# -*- coding:utf-8 -*-
"""
作者：KYLE
日期：2021年08月22日
"""

# 打印任务的属性：提交时间（每秒, 1/180个作业或者 每180秒1个作业），打印页数（1-20页，随机）,需要打印的时间
# 队列属性：先进先出
# 打印机的属性：打印速度（每分钟多少页）快则质量低（最后需要得出，全部都能打印出来），是否忙（如果忙则等待，如果不忙则立即打印）,下一个任务的情况
# 1. 需要等待时间短
# 2. 全部都打印

# 操作过程
# 创建打印队列
# 2. 按照概率生成打印作业，加入打印队列
# 3. 如果打印机空闲，且队列不空，则取出队首作业打印，记录次作业等待时间
# 4. 如果打印机忙，则按照打印速度进行1秒打印 （这里就很精妙！！用流逝的时间代表打印动作）
# 5. 如果当前作业打印完成，则打印机进入空闲
# 时间用尽，开始统计平均等待时间
# 作业等待时间
# 生成作业时，记录生成时间戳
# 开始打印时，当前时间减去生成时间即可
# 作业的打印时间
# 生成作业时，记录作业的页数
# 开始打印时，页数除以打印速度即可（

from Queue import Queue
import random

class Printer:
    def __init__(self,ppm):
        self.paperate = ppm
        self.currentTask = None #初始化时没有打印任务
        self.timeRemaining = 0 #打印任务的剩余时间

    def tick(self): #打印1秒
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <=0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask): #传入一个任务，包括了创建时间，花费时间，页数
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 /self.paperate

class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self,currenttime):
        return currenttime - self.timestamp

def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

def simulation(numSeconds,pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waittingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond) #task包含生成时间，打印页数
            printQueue.enqueue(task)


        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waittingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask) #

        labprinter.tick()

    averageWait = sum(waittingtimes) / len(waittingtimes)

    print("average Wait %6.2f secs %3d task remaining."%(averageWait,printQueue.size()))




if __name__ == '__main__':
    # 1. 热土豆问题
    # print('最后留下的一人是：',hotPotato(list(range(1,41)),0))
    # 2. 打印任务
    for i in range(10):
        simulation(3600, 5)
