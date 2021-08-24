# -*- coding:utf-8 -*-
"""
作者：KYLE
日期：2021年08月22日
"""


from Queue import Queue


def hotPotato(namelist, num):
    q = Queue()

    # 将列表中的内容加入队列
    for name in namelist:
        q.enqueue(name)

    # 传递一次，即表示将队首出列加入队尾；此时队首之人就是拿着土豆的人==>出列。
    # 一直循环执行，直到队列中只有1人时，结束。
    while q.size() > 1:
        for i in range(num):  # num是几，就表示传递几次
            q.enqueue(q.dequeue())
        q.dequeue()  # 拿到土豆的人出列，继续进行下一圈

    return q.dequeue()


#------------------------整个打印机设计都是极其精妙的，现阶段我肯定写出来-----------------------------
# 打印任务的属性：提交时间（每秒, 1/180个作业或者 每180秒1个作业），打印页数（1-20页，随机）
# 队列属性：先进先出
# 打印机的属性：打印速度（每分钟多少页）快则质量低（最后需要得出，全部都能打印出来），是否忙（如果忙则等待，如果不忙则立即打印）
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

import random

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm  # 打印速度设置，单位 页数/分钟
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):  # 这里非常精妙，用时间流逝代表1秒，代表打印动作1秒
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond) #task就包含两个属性：生成任务时间，打印页数
            printQueue.enqueue(task)   #task加入队列

        # 如果打印机空闲，且打印队列不为空==>则将打印队列的任务出队，进行相应计算。
        # 如果打印机正在忙着，则跳过次步骤（正常打印1秒）
        # 如果打印任务队列也是空的，则跳过则步骤（正常打印（度过）1秒，任务队列没有变化）

        if (not labprinter.busy()) and (not printQueue.isEmpty()): #如果打印机空闲且队列不为空
            nexttask = printQueue.dequeue() #现有的队首任务出队的是，nexttask是Task对象：包含了生成时间，页数、等待时间
            waitingtimes.append((nexttask.waitTime(currentSecond))) # 等待时间= 当前时间-生成时间
            labprinter.startNext(nexttask) #startNext两个属性：nexttask（Task对象），下个任务花费的时间。相当于给labprinter赋值CurrentTask=task和timereaiming.

        labprinter.tick() #打印1下（1秒）

    averageWait = sum(waitingtimes) / len(waitingtimes)
    print("Average Wait %6.2f secs %3d task remaning." % (averageWait, printQueue.size()))


if __name__ == '__main__':
    # 1. 热土豆问题
    # print('最后留下的一人是：',hotPotato(list(range(1,41)),0))
    # 2. 打印任务
    for i in range(10):
        simulation(3600, 10)
