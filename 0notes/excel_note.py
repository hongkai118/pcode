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

#将matplotlib图表写入excel表格里
#import matplotlib.pyplot as plt
#%matplotlib inline
#fig = plt.figure()
#plt.plot([1,2,3,4,5])
#sht.pictures.add(fig,name='MyPlot',update=True)