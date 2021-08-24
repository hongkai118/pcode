
2. 数据类型的性能
    》list性能
        index[]                 O(1)
        index assignment        O(1)
        append                  O(1)
        pop()                   O(1)
        pop(i)                  O(n)
        insert(i,item)          O(n)
        del operator            O(n)
        iteration               O(n)
        contains(in)            O(n)
        get slice[x:y]          O(k)
        del slice               O(n)
        set slice               O(n+k)
        reverse                 O(n)
        concatenate             O(k)
        sort                    O(n log n)
        multiply                O(nk)
        
    》dict性能
        copy                    O(n)
        get item                O(1)
        set item                O(1)
        delete item             O(1)
        contains(in)            O(1)
        iteration               O(n)    
        
3. 线性结构
    》栈
        》特点：加入和移除都发生在同一端，叫栈顶；例如：盘子叠起来，书堆等等
        》次序：后进先出Last in First Out
        》应用：
            》浏览器后退功能
            》Office的撤销功能
        》“栈”：定义为如下操作：
            Stack(): 创建一个空栈、不包含任何数据项
            push(item):将item加入栈顶，无返回值
            pop():将栈顶数据移除并反馈；栈被修改
            peek():“窥知”栈顶数据项，返回栈顶的数据项但不一处，栈不被修改
            isEmpgy():返回栈是否为空栈
            size():返回栈中有多少个数据项
        》栈的应用
            》简单括号匹配：
                1）生成一个空栈
                2）从左到又依次取括号
                    a.左括号：加入栈顶
                    b.右括号：栈空么
                        ——不空：从栈顶移除
                        ——空：匹配失败
                3）栈空了：匹配成功
                
            》进制转换
                》二进制转换
                    》普通数字除以2求余数，继续除2就余数，一直到最后
                    》将得到的余数次序反转得到的数字。
                》其他进制：
                    》只需要将“除以2求余数”算法改为“除以N求余数”算法就可以了
                    》常用的有16进制和8进制
            》表达式转换（p18,没看懂)
    》队列Queue
        》特点：有次序的数据集合
            》数据从尾款添加，从首端移除
            》先进先出
            
        》例子：
            》排队
            》打印
            》操作系统进程调度
        》队列的操作定义：
            Queue():创建一个空队列对象，返回值为Queue对象
            enqueue(item)：将数据项item添加到队尾，无返回值
            dequeue():从队首移除数据项，返回值为队首数据项，队列被修改；
            isEmpty():测试是否空队列，返回值为布尔值
            size():返回队列中数据项的个数
        
                    
                  
                