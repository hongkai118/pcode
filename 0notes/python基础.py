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
            1）文本的表示
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
                    '-'.join(['a','b','c']) #返回字符串'a-b-c'
                
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

    ——可变和不可变类型
        ——不可变（immutable):int、float、复数、字符串、逻辑值、元组
        ——可变类型：列表、字典、集合
            ——实例：列表赋值是创建了标签，并没有复制一份。
                a=[1,3,4,5] 
                b=a
                print(b); #[1,3,4,5]
                a.append(6) #修改a后,b也跟着改变
                print(b); #[1,3,4,5,6]



3. 控制流语句
    if, while, for

4. 定义语句
    def, class