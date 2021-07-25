# -*- coding:utf-8 -*-
"""
作者：KYLE
日期：2021年07月10日
"""

1. 数据类型
    —— 数据基本类型  
        ——数值
            1) int
                ——最大特点：不限制大小
                ——最常见运算：
                    +, -, * , / 
                    //：商的整数部分
                    % ：求余数部分
                    divmod(m,n): 会得到两个整数：m//n和m%n
                    m**n: m的n次方
                    abs(m): 绝对值
                ——大小比较：==, >, <, >=, <=, 
                ——连续判断：
                    7>3>2 #True
                    7>3>6: #False
                ——各种进展表示：
                    ——十进制： 正常书写
                    ——二进制bin()： 0b101010
                    ——八进制oct()： 0o557
                    ——十六进制hex()：0x16f
            
            2) float
                ——最高17位有效位数。
                ——进制转换精度误差。
            
            3) 复数(我自己应该用的少)
                ——书写方法：a+bj

            4）其他：数学模块
                —— math：计算整数和浮点数
                —— cmath:处理复数       
        ——逻辑值(bool)
            1）逻辑运算优先级：not最高，and次之，or最低。（如果运算过于复杂，建议用括号括起来更易于阅读。
            2）各种类型对应的逻辑值：
                ——0是“假”，所有非0都是”真“，
                ——空字符串是“假”，所有非空字符串都是”真“
                ——空序列是“假”，所有非序列串都是“真”
                ——空值None，表示”无意义“或”不知道“，也是”假“
        ——字符串
            1) 文本的表示
                —— 把一个个字符“串起来“的数据，字符包括中文、英文、数字、标点等
                —— 转义符: \ 
                ——字符串编号从0开始表示第1位，-1表示倒数第1位：取值方法string[0],string[-1]
            2) 字符串操作
                —— 长度：len(string)
                —— 切片(slice)：s[start:end:step],如s[3:8:2],s[3:8 ]
                —— +：拼接字符串
                —— *：如'abc'*5,表示"abcabcabcabcabc" 
                —— in: 'h' in 'hexe' #True
                —— ==: 'abc'=='abc' #True
                —— 删除空格
                    —— str.strip()：去掉字符串前后的所有空格，内部空格不受影响
                    —— str.lstrip(): 去掉字符串左边的所有空格
                    —— str.rstrip(): 去掉字符串右边的所有空格
                —— 判断字母数字：
                    ——str.isalpha:判断是字符串是否全部由字母构成
                    ——str.isdigit:判断是字符串是否全部由数字构成
                    ——str.isalnum:判断是字符串是否仅包含字母和数字，而不含特殊字符。

                —— split：分割后返回list。
                    实例1：
                    'you are my sunshine.'.split(' ') #返回列表['you','are','my','sunshine.']

                —— join：列表合并为字符串
                    实例1：
                    '-'.join(['a','b','c']) #返回字符串'a-b-c'，list的项只能是字符串类型
                
                —— upper/lower/swapcase:字母大小写处理
                    实例1：
                    'abc'.upper() #ABC
                    'aBC'.lower() #abc
                    'aBC'.swapcase() #Abc 反转大小写
                
                —— ljust/center/rjust: 左对齐/右对齐/居中对齐

                —— replace: 替换
                    实例1：
                    'tom simled, tom cried, tom shouted'.replace('tom','jane') #'jane simled, jane cried, jane shouted'
                —— ord(),chr():ord()字符转变成编码，chr()编码反过来 
            
            3) 字符串是一种序列(sequence)：

        ——序列
            —— 特征：能够按照整数顺序排列的数据
            —— 序列的内部结构（所有序列可以进行一下操作，list也应也是序列）
                ——可以通过0开始的连续整数来索引单个对象
                ——可以执行切片，获取序列的一部分
                ——可以通过len函数获取包含多少元素
                ——可以用”+“来连接
                ——可以用"*"来重复多次
                ——可以用“in”来判断单个元素是否再序列中存在
                        
    —— 容器类型
        ——列表list和元组
            ——列表和元组也是序列，继承了序列的所有特别如，索引、切片、len、in 等等
            ——特性：可以删除、添加、替换、重排；列表可变序列，元组是不可变序列。
            ——操作：
                ——创建
                    ——列表：li=[], 或者list(li)
                    ——创建元组：(), 或者tuple()
                ——增加元素：
                    ——li.append(item):增加再最后
                    ——li.insert(i,item):插入
                
                ——删除列表和元素
                    ——li.pop()/pip(i): pop()删除最后一个元素，pop(i)删除第i个元素并返回值。
                    ——del li[i]:删除第i个元素
                    ——li.remove(item)：删除首次出现的item
                    ——li.clear():变为空列表

                ——排序：
                    ——li.reverse():反转，按照元素的位置从头到尾重新排列，如li=[9,8,1,3,0], li.reverse(), 返回[0,3,1,8,9]
                    ——li.sort():
                        ——正序，如li.sort()，按照元素的值从小到大。返回[0,1,3,8,9]
                        ——倒序，如li.srot(reverse=True),按元素值从大到小排序，返回[9,8,3,1,0]
                ——合并列表
                    —— extend():合并两个列表，改变了原来的列表
                    —— 加法+：连个列表不变，生成一个新列表（元组）
                    —— 乘法*：复制n次，生成新的列表（元组） 
                ——其他方法：
                    ——li.index(item):找到item的首次数显位置
                    ——li.count(item):找到item再列表中出现的次数
                    ——查找：同字符串用in 查找
                    ——sum函数：将列表中所有元素累加
                    ——min/max函数：返回李彪中最小/最大的数据元素
                    
        ——字典dict
            ——特性：数据项（item)：表key:value的键值对。
                ——字典是可变类型
                ——没有顺序，
                ——key:value可以是任意类型
                ——可以，删除、添加、替换、len()、in等操作
            ——操作：
                ——创建字典：student={},或student=dict()              
                ——增和改：
                    ——update:student.update(item),更新字典
                    ——直接赋值：student['name']='tom'
                ——删
                    ——del: del student[key], 删除指定标签的item
                    ——pop：student.pop(key):删除指定标签item并返回value
                    ——popitem:student.popitem():随机删除并返回：item的元组方式如(key,value)
                    ——clear:student.clear() 清空字典
                ——查
                    ——student[key]:通过key获取value

                ——重要方法：
                    ——keys：student.keys();返回字典中所有的key的列表
                    ——values：student.values();返回字典中所有value的列表
                    ——items:student.items()；返回字典中所有的(key,value)的列表
                    ——in操作：key in student 或 value in student.values()
                    ——len操作：len(student):返回大小
                
        ——集合set
            ——特性：
                ——无序、不重复的组合
                ——会自动忽略重复数据
                ——不能加入可变类型数据
            ——创建集合：{}或set()
                ——创建空集合
                ——其他序列转换为集合
            ——操作：
                ——增：
                    ——add:添加；aset.add(vlue)
                    ——update:
                ——删：
                    ——remove/discard: aset.remove(value) 删除指定数据
                    ——pop: aset.pop() 删除任意数据并返回值
                    ——clear:aset.clear() 清空集合
                ——常用方法：
                    ——len操作：len(aset) 函数
                    ——in操作
                    ——迭代循环：for a in aset:

                ——集合的运算
                    ——生成新集合
                        ——合：a|b
                        ——交：a&b
                        ——差：a-b
                        ——对称差: a^b ，返回去掉交集的部分
                    ——关系判定
                        —— <=：子集
                        —— <：真子集
                        —— >=：超集
                        —— >：真超集
                    ——交集
                        ——isdisjoint():两集合交 集为空返回 True，
            ——使用场景：
                ——快速去重复数据项
                ——集合的“in判断”效率很高
                ——对数据次序不关心时，集合的性能比列表高很多

    —— 可变和不可变类型
        ——不可变（immutable):int、float、复数、字符串、逻辑值、元组
        ——可变类型：列表、字典、集合
            ——实例：列表赋值是创建了标签，并没有复制一份。
                a=[1,3,4,5] 
                b=a
                print(b); #[1,3,4,5]
                a.append(6) #修改a后,b也跟着改变
                print(b); #[1,3,4,5,6]



2. 计算和控制流语句（if, while, for）
    —— 计算：赋值语句
    —— 容器：三种结构（所有语言都有这三种结构）：
        ——顺序结构
        ——条件分支结构(if,elif,else)
        ——循环结构
            ——while 语法：
                while <逻辑表达式>:
                    <语句块>
                    break #跳出循环
                    continue #掠过当下循环语句，继续检查while进行循环
                else:    #只有while逻辑表达式为假的时候会执行，如果时break退出时不执行
                    <语句块>
            ——for 语法：
                for i in <可迭代对象>：
                    <语句块>
                    break #跳出循环
                    continue #掠过余下循环语句
                else: #迭代完毕，则执行
                
    ——代码组织：函数
        ——封装：
            ——容器是对数据的封装
            ——函数是对语句的封装
            ——类是对方法和属性的封装

        ——函数(function)
            ——def创建、return 返回值
            ——调用函数
            ——变量
                ——局部变量
                ——全局变量
            —— 函数小技巧
                ——map()函数：map(func,list1,list2...), #func是函数传入，有几个参数就传几个列表。
                    ——实例1：
                    num=[10,20,40,80,160]
                    lst=[2,4,6,8,10]
                    def mul3(a):
                        return a*3
                    print(list(map(mul3,num))) #结果[30,60,120,240,480]
                    
                    def atob(a,b)
                        return a+1.0/b
                    print(list(map(atob,num,lst))) #结果[10.5, 20.25, 40.166666666666664, 80.125, 160.1]
                ——lambda匿名函数:只需要调用一次的函数，不用专门去创建函数，起个匿名函数就可以
                    ——实例：
                        print(list(map(lambda a:a*3,num)))
                        print(list(map(lambda a,b:a+1.0/b,num,lst)))
            
            —— 参数
                ——形式参数：定义的时候扩号里面的
                    ——固定参数：如 def func(key1,key2,key3) #确切的知道有几个值传进来
                    ——可变参数：
                        ——def func(*args): #不带key的多个参数 
                            ——实例：
                            def func_test2(*args):
                                for arg,i in zip(args,range(len(args))):
                                    print("arg%d=%s"%(i,arg) 
                            func_test2(12,34,'abcd',True)
                            #输出arg0=12 arg1=34,arg3=abcd,arg4=True)
                            
                       
                        ——def func(**kwargs):#key=value 形式的多个参数
                            ——实例：
                            def func_test3(**kwargs):
                                for key,val in kwargs.items():
                                    print("%s=%s"%(key,val))
                            func_test3(myname="tom",sep="comma",age=23)
                            #输出：sep=comma,age=23,myname=tom
                ——实际参数：具体的值，调用函数时赋值。 
                 
    ——引用扩展模块：
        ——定义：每个扩展名为.py的python程序就是一个独立的模块
        ——调用：
            ——import <模块> [as <别名>]
            ——from <模块> import <函数>
    ——标准库：
        ——定义：在安装python时默认安装好的模块。
        ——数学和数学模块：math,cmath,等等
        ——数据类型：datetime,calendar,
        ——功能编程模块：
            ——itertools:
            ——functools:
            ——opreator:
        ——数据持久化：
            ——pickle:python对象序列化
            ——copyreg:注册pickle
            ——sqlite3:sqllite数据库的DB-API
        ——数据压缩和存档：
        ——文件格式：csv等
        ——文件和目录访问：
            ——pathlib:面向对象的文件系统路径
            ——os.path:常见路径名操作
            ——fileinput
            等
        ——通用操作系统服务：os,io,time,argparse,curses等等
        ——并发执行：
            ——threading:线程
            ——multiprocessing:进程
            等等
        ——加密：
            ——hashlib
            ——hmac
            ——secrets
        ——网络服务
            ——asynico:异步
            ——socket:
            等等   
        ——互联网数据处理：email,json,mailcap等等
        ——互联网协议和支持：webbrowser,cgi,urllib等等
        ——多媒体服务：audioop,aifc,sunau,wave等等
        ——标记语言的处理：html,xml等等
        ——程序框架：turtle,cmd,shlex等
        ——图形界面：tkinter: Tcl/Tk的python接口 
    ——命名空间:
        ——dir(<名称>)函数：列出名称的属性
        ——help(<名称>)函数：显示参考手册
        
3. 基本扩展模块
    ——时间相关
        ——datetime模块
            ——主要的类
                ——datetime.date() #处理日期（年月日）
                ——datetime.time() #处理时间（时分秒、毫秒）
                ——datetime.datetime() #日期+时间
                ——datetime.timedelta() #时间间隔
            ——获取当前时间
                ——获取今天时间：
                    —— datetime.date.today() #输出 datetime.date(2021, 7, 21)
                    —— datetime.datetime.now() #输出 datetime.datetime(2021, 7, 21, 21, 55, 52, 168805)
                ——调整日期格式：
                    —— datetime.date.today().strftime('%Y-%m-%d %H:%M:%S') #输出'2021-07-21 00:00:00'
                    —— datetime.datetime.now().isoformat() #输出'2021-07-21T21:58:20.958081'
            
            ——时间戳
                ——概念：格林威治时间1970年1月1日0时0分0秒到现在的总秒数
                ——将日期转换成时间戳
                    ——timetuple函数：将时间转换成stuct_time格式
                        ——datetime.date.today().timetuple() #输出元组格式为元组如下一行，直接操作元组的方式。time.struct_time(tm_year=2021, tm_mon=7, tm_mday=21, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=202, tm_isdst=-1)
                        ——datetime.date.today().timetuple()[0:] #上面的实例，输出为(2021, 7, 21, 0, 0, 0, 2, 202, -1)
                    ——time.mktime函数：返回用秒数来表示时间的浮点数
                        ——time.mktime(datetime.date.today().timetuple()) #返回时间戳浮点数1626796800.0
                    ——formtimestamp(时间戳)：输入时间戳，返回时间格式。
                        datetime.date.fromtimestaple(时间戳) #返回dateime.date(2020,10,9)
                        
            ——时间上的加减法
                ——timedelta()方法：表示两个时间点的间隔
                    ——实例
                    >>> today=datetime.datetime.now()
                    >>> yesterday=today-datetime.timedelta(days=1)  #days参数，变量
                    >>> print(yesterday) #输出2021-07-20 22:14:13.453367
                    >>> hours=today-datetime.timedelata(hours=1)  ##hours是参数，变量
                    >>> print(hours)#输出2021-07-21 21:14:13.453367                   
        ——calendar模块、
            ——常用函数：
                ——calendar.calendar(<年>)#显示一整年日历
                ——calendar.month(<年>,<月>)#显示一个月的日历
                ——calendar.prmonth(<年>,<月>) #显示一个月的日历
                ——calendar.prcal(<年>) #显示一整年日历
                ——calendar.monthcalendar(<年>,<月>) #返回一个月的嵌套列表，里层7个元素代表一周（从周一到周日），没有本月的日期，则为0
                ——calendar.isleap(<年>) #判断闰年，如calendar.isleap(2018) 返回False不是闰年
                    ——普通闰年：能被4整除但不能被100整除的年
                    ——世纪闰年：能被400整除的年
                ——calendar.monthrange(2018,9) #计算某月从周几开始，有多少天；返回(5,30)
                ——calendar.weekday(2018,8,15) #计算某天是星期几，返回值0-6，对应周一到周日
        ——time模块
            ——时间戳：time.time() #设置两个可以相减，可以计算程序时间。
            ——获取当前时间：
                ——time.astime()#输出'Sun Jul 25 07:19:47 2021'
                ——time.ctime() #输出'Sun Jul 25 07:19:47 2021'
            ——将元组转化为时间：
                ——代码：
                t=(2018,8,3,11,42,31,0,0,0)
                time.asctime(t) #'Mon Aug  3 11:42:31 2018'
            ——struct_time类    
                ——time.localtime() #输出一个元组，可以像元组一样访问年月日时分秒time.struct_time(tm_year=2021, tm_mon=7, tm_mday=25, tm_hour=7, tm_min=23, tm_sec=50, tm_wday=6, tm_yday=206, tm_isdst=0)
    ——算术模块
        ——math模块：支持浮点数
        ——cmath模块：支持复数运算
        ——decimal模块：固定精度小数         
            from decimal import Decimal
            Decimal(0.1) #生成一个小数
            #小数计算
            Decimal(0.1)+Decimal(0.1)-Decimal('0.2') #输出Decimal('0.00')
        ——fractions模块：分数
            #生成分数
            from fractions import Fraction
            Fraction(1,4) #或者Fraction('0.25')
            
            #浮点数转为分数
            Fraction.from_float(1.75) #会有误差
        ——random模块：（伪）随机数
            ——random():生成范围[0,1)之间的随机实数
            ——uniform(a,b):生成[a,b)之间的随机浮点数
            ——randint(m,n):生成[m,n]内的整数
            ——randrange(a,b,n):可以在[a,b)范围内,按n递增的集合中随机选择一个数
            ——getrandbits(k)：生成k为二进制随机整数，如getrandbits(2)=>生成0，4的整数，getrandbits(10)=》生成0到1024的整数
            ——choice():从指定序列中随机选择一个元素
            ——sample():指定每次随机元素的个数
            ——shuffle():可以将可变序列重新洗牌
            ——代码：
                >>> colors=['red','blue','green','black']
                >>> random.choice(colors)
                'black'
                >>> random.sample(colors,2)
                ['black', 'red']
                >>> random.shuffle(colors)
                >>> colors
                ['green', 'red', 'black', 'blue']    
    ——文件读写
        ——文本文件：txt
            ——open()函数：
                ——打开文件：f=open(filename[,mode[,buffering]]) #buffering默认时-1可以不写
                    ——mode第一个字母:
                        ——'r'读模式，
                        ——'w'写模式,
                        ——'x'文件不存在时创建并写文件
                        ——'a'在文件末尾追加写内容
                        ——'+'表示读写模式
                    ——mode第二个字母:    
                        ——'t'表示文本文件
                        ——'b'表示二进制文件
                ——文件的写操作：
                    ——f.write(str)
                    ——f.writelines(strlist):写入字符串列表
                ——文件的读操作：
                    ——f.read()
                    ——f.readline():读一行
                ——文件的关闭：f.close()
            
            ——with open:#上下问管理器更优秀,会自动关闭文件
                ——使用方法：
                    with open('1.txt','r') as f:
                        f.read()
        ——结构化文本文件：csv
            ——文件读取：
                —— re=csv.reader() #接受一个可迭代对象（如csv文件），返回一个生成器，可以从其中解析内容
                —— re=csv.DictRead() #与reader类似，返回的值，元组保存
            ——文件写操作：
                —— w = csv.write()
                —— w = writerrow(rows)                  
                ——文件不存在时自动生成；支持单行和多行写入
            ——字典数据写入：
                —— w=csv.DictWriter()
                —— w.writeheader()
                —— w.writerow(rows)
        ——excel文件：
            ——xlwings笔记和实例代码：
                import xlwings as xw
                wb = xw.Book("D:\PP\Code\excel\example.xlsx")
                sht = wb.sheets["ss2"]
                wb.fullname
                print('wb.fullname:',wb.fullname)
                sht.name
                print('sht.name:',sht.name)

                #自己犯过的错误，xlwings卡死，结果不是xlwings的问题，而是解析网页时获取的值，没有数据，组合成列表时卡死了。

                #创建excel
                wb=xw.Book()

                #获取表格列行大小，返回（行，列）
                #方法1
                sht.range('A1').expand().shape
                #方法2，反馈（行，列）
                sht.used_range.shape
                #方法3
                sht.used_range.last_cell.row #行
                sht.used_range.last_cell.column #列

                #在单元格中写入数据
                sht.range('a1').value='随'

                #读取单元格内容
                tt=sht.range('a1').value
                print(tt)

                #清楚单元格内容和格式
                #sht.range('a1').clear()

                #获取单元格的列标
                aa=sht.range('c10').column
                print(aa)

                #获取单元格行标
                bb=sht.range('c10').row
                print(bb)

                #自适应
                sht.range('C10').autofit()

                #给单元格上色
                sht.range('C10').color =(34,139,34)

                #获取单元格颜色
                cc=sht.range('C10').color
                print(cc)

                #清除单元格颜色
                sht.range('c10').color = None

                #以下两种方式都可以输入公式
                sht.range('c12').formula ='=sum(b7:b9)'

                sht.range('c14').value='=sum(b7:b8)'

                #获取单元格公式
                dd=sht.range('c14').formula_array
                print(dd)

                #获取单元格数值
                ee=sht.range('c14').value
                print(ee)

                #再单元格中写入批量数据，只需要指定其单元格位置
                sht.range('a2').value = [['foo 1','foo 2','foo 3'],[10.0,20.0,30.0]]

                #读取表中批量数据，使用expand()方法
                ff=sht.range('A2').value
                print(ff)

                hh=sht.range('a2').expand().value
                print(hh)

                #保存文档
                sht.save()
                wb.close()


                #可以不指定工作表，直接与活动表格交互
                #写入
                #xw.Range('E1').value='xlwings'
                #xw.Range('E1').value

                #支持numpy、pandas\ matplotlib
                #支持写入numpy array 数据类型
                import numpy as np
                np_data = np.array((1,2,3))
                sht.range('f1').value = np_data

                #支持将pandas DataFrame数据写入excel
                import pandas as pd
                df = pd.DataFrame([[1,2],[3,4]],columns=['a','b'])
                sht.range('A5').value=df
                print(df)

                #将数据读取,输出类型为DataFrame
                ii=sht.range('A5').options(pd.DataFrame,expand = 'table').value
                print(ii)
        ——PDf文件：
            ——PyPDF2库介绍：基础教程中中没有代码，需要用到的时候，去网上搜新的教程。

    ——图形界面模块GUI：
        ——easygui模块    
        
    ——海归作图：
        ——turtle模块：内置模块随时可用    
        ——属性：位置、方向、画笔（颜色、线条宽度等）
        ——指令：
            ——画笔运动命令：前/后移动、左右转动、作画速度等
            ——画笔空值命令：抬起/放下、画笔宽度、颜色、填充颜色等
        ——实例：
            ——画一个三角形
                import turtle #导入turtle模块
                p=turtle.Pen() #创建一支画笔（海龟）
                p.pencolor('blue') #设置画笔为蓝色
                p.pensize(5) #画笔粗细为5
                p.forward(100) #最初画笔（海龟）朝向正右方，向前画长度100的直线
                p.left(120) #左转120度
                p.forward(100) #向前运动100
                p.left(120) #左转120度
                p.forward(100) #向前运动120
                p.left(120) #左转120，变为初始方向
                turtle.done() #保持画图窗口不退出
                
            ——画五角星：
                import turtle
                t= turtle.Pen() #也可以 t=turtle.Turtle()
                # w= turtle.Screen() 
                for i in range(5):
                    t.forward(100)
                    t.right(144)
                turtle.done()
                            
    
            ——画二叉树(分型图)：
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

                if __name__=='__main__':
                    t= turtle.Turtle() #生成海龟
                    myWin=turtle.Screen()
                    t.left(90) #海龟朝向正北
                    t.up() #抬起海龟
                    t.backward(200) #回退200具体
                    t.down() #放下海龟
                    t.color('green') #设置颜色
                    tree(150,t) #条用话术的颜色
                    myWin.exitonclick()
        ——分形图(用迭代可画)：
            ——曼德勃罗集
            ——hilbert曲线
            ——谢尔宾斯基三角形
    
    
 
4. 常见函数
    ——range()：range(<起点>,<终点>,<步长>)