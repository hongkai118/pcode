

      
open用法：打开文件模式：
    --'w', 写模式，如果没有文件创建文件
    --'r', 读模式，没有文件会报错
        --f.read(),读取文件内容
        --f.readline(),读取一行
        --f.readlines()，输出列表，读取所有行。
    --'a'，在末尾追加
    --'b', 二进制模式

f=open('1.txt','r')
for line in f:
    print(line) #类似readline()功能


json用法：处理字典文件
    ——首先import json
    ——需要先用open打开文件，再用json.load(file)读取，实例代码如下：
    with open('company_dics.json','r',encoding='utf-8') as fp:
        com_dic=json.load(fp)  #com_dic即为字典。
    ——注意事项，自己建立json文件时，key-value,一定要使用双引号
    




import os 
from pathlib import Path

#os模块
os.getcwd() #返回当前的工作目录
os.listdir(path) #返回指定路径下的文件和目录，列表。
os.mkdir(path[,mode=]) #创建目录
os.makedirs(path1/path2...[,mode]) #创建多级目录
os.remove(path) #删除文件
os.rmdir(path) #删除目录
os.removedirs(path1/path2...) #删除多级目录
os.chdir(path) #将path设置为当前工作目录
os.scandir(path) #返回迭代器，包括文件和目录
    ——.is_file() #迭代对象方法，判断是否为文件
    ——.is_dir() #迭代对象方法，判断是否为目录
os.walk(path) #反馈一个迭代对象包括:dirpath,dirname,filename.
os.rename(old_name,new_name)

#os.path模块
abspath(path) #返回绝对路径
exists(path) #判断文件或目录是否存在
join(path,name) #将目录与目录或者文件名拼接起来
splitext(path) #分离文件名和扩展名，返回元组('d:\\dir\\dir\\filename','.doc)
split(path) #分离目录和文件名，返回元组('d:\\dir\\dir','filename.doc')
basename(path) #从一个目录中提取文件名
dirname(path) #从一个路径中提取文件路径，不包括文件名
isdir(path) #判断是否为目录

#移动文件。巨坑！！！！
# 一定要配合创建目录使用！！
# 如果没有目标目录不存在，会直接创建一个文件。
# 所有移动的文件都会覆盖在new_dir文件名里面（等于删除，而且无法恢复）
#创建文件目录
def create_dir(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)
create_dir(new_dir)
shutil.move(old_file,new_dir) 
