# -*- coding:utf-8 -*-
"""
作者：KYLE
日期：2021年05月26日
"""
from django.shortcuts import HttpResponse,render,redirect
import pymysql

# def mysql_select(sql_select):
#     conn = pymysql.connect(host='127.0.0.1', port=3306, user='k1', passwd='123', db='db10', charset='utf8')
#     cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#     cursor.execute(sql_select)
#     result = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return result


# def mysql_insert(sql_insert):
#     conn = pymysql.connect(host='127.0.0.1', port=3306, user='k1', passwd='123', db='db10', charset='utf8')
#     cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#     cursor.execute(sql_insert)
#     conn.commit()
#     cursor.close()
#     conn.close()


def index(request):
    # return render(request,'index.html')
    return render(request,'index.html',{
        'name':'kkk',
        'users':['y1','y2','y3'],
        'user_dict':{'k1':'v1','k2':'v2','k3':'v3'},
        'user_list_dict':[
            {'id':1,'name':'yy1','email':'you1@163.com'},
            {'id':2,'name':'yy2','email':'you2@163.com'},
            {'id':3,'name':'yy3','email':'you3@163.com'},
            {'id':4,'name':'yy4','email':'you4@163.com'},
            {'id':5,'name':'yy5','email':'you5@163.com'}
        ]
    })



def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        user = request.POST.get('username')
        pwd = request.POST.get('pwd')
        if user == 'root' and pwd == '123':
            return HttpResponse('恭喜你登录成功')
        else:
            return render(request,'login.html',{'msgg':'账号或密码不对'})

from utls import sqlhelper


def classes(request):
    '''
    在网页中显示所有班级
    :param request:
    :return:
    '''

    #获取数据库数据
    # conn = pymysql.connect(host='127.0.0.1', port=3306, user='k1', passwd='123', db='db10', charset='utf8')
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # cursor.execute("select id,class from class")
    # class_list = cursor.fetchall()
    # # print(class_list)
    # cursor.close()
    # conn.close()
    class_list = sqlhelper.get_list("select id,class from class",[])

    #再进行模板渲染
    return render(request, 'classes.html', {'class_list': class_list})

def add_classes(request):
    #1. 获取网页传输回来的数据
    #2. 添加到数据库
    #3. 展示到classes网页

    if request.method == 'GET':
        return render(request,'add_classes.html')
    else:
        v = request.POST.get('class_name')
        # conn = pymysql.connect(host='127.0.0.1', port=3306, user='k1', passwd='123', db='db10', charset='utf8')
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # cursor.execute("insert into class(class) values (%s)", [v,])
        # conn.commit()
        # cursor.close()
        # conn.close()
        sqlhelper.modify("insert into class(class) values (%s)", [v,])

        return redirect('/classes/') #这里访问的是Url（意思访问函数）就有值，传给classes页面了
        # return render(request,'classes.html') #这里访问的是直接访问的classes模板文件，没有传递值进来，所有值白板。

def del_classes(request):
    #1. 获取网页传过来的值
    nid = request.GET.get('nid')

    #2. 连接数据库，删除数据
    # conn = pymysql.connect(host='127.0.0.1', port=3306, user='k1', passwd='123', db='db10', charset='utf8')
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # cursor.execute("delete from class where id=%s", [nid,])
    # conn.commit()
    # cursor.close()
    # conn.close()
    sqlhelper.modify("delete from class where id=%s", [nid,])

    #3. 返回url（函数）班级列表
    return redirect('/classes/')

def edit_classes(request):

    g_nid = request.GET.get('nid')
    #0. 通过GET请求时正常显示网页，取得相关数据, 展示在编辑页面
    if request.method =='GET':

        # conn = pymysql.connect(host='127.0.0.1', port=3306, user='k1', passwd='123', db='db10', charset='utf8')
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # cursor.execute("select id,class from class where id=%s",[g_nid,])
        # result = cursor.fetchone()
        # cursor.close()
        # conn.close()
        # print(result)
        result=sqlhelper.get_one("select id,class from class where id=%s",[g_nid,])

        return render(request,'edit_classes.html',{'result': result})

    else:
        #1. POST传来的数据，提交到库--反馈到classes页面展示
        id = request.GET.get('nid')
        edit_n=request.POST.get('edit_n')
        # print('id',id)
        # print('edit_n',edit_n)

        #2. 连接数据库，编辑数据
        # conn = pymysql.connect(host='127.0.0.1', port=3306, user='k1', passwd='123', db='db10', charset='utf8')
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # cursor.execute("update class set class=%s where id=%s", [edit_n,id,])
        # conn.commit()
        # cursor.close()
        # conn.close()
        sqlhelper.modify("update class set class=%s where id=%s", [edit_n, id,])

        return redirect('/classes/')

def teacher(request):
    #连接数据库，获得数据，展示到网页
    teacher_list=mysql_select("select id,t_name from teacher")
    print(teacher_list)

    return render(request,'teacher.html',{'teacher_list':teacher_list})

def add_teacher(request):
    #get访问就显示添加页面
    if request.method =='GET':
        return render(request,'add_teacher.html')


    else:
        #获取网页数据，插入数据库，跳转到teacher页面显示
        v = request.POST.get('t_name')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='k1', passwd='123', db='db10', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("insert into teacher(t_name) values (%s)", [v,])
        conn.commit()
        cursor.close()
        conn.close()
        # mysql_insert("insert into teacher(t_name) valuse(%s)",[v,])

        return redirect('/teacher/')

def del_teacher(request):
    t_id = request.GET.get('t_id')
    #连接数据库
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='k1', passwd='123', db='db10', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("delete from teacher where id=%s", [t_id,])
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/teacher')

def edit_teacher(request):

    if request.method == 'GET':
        t_id = request.GET.get('t_id')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='k1', passwd='123', db='db10', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select id,t_name from teacher where id=%s",[t_id,])
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        # print(result)

        return render(request,'edit_teacher.html',{'result':result})

    else:
        t_id = request.GET.get('t_id')
        t_name =request.POST.get('t_name')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='k1', passwd='123', db='db10', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("update teacher set t_name=%s where id=%s",[t_name,t_id])
        conn.commit()
        cursor.close()
        conn.close()

        return redirect('/teacher/')



def student(request):
    #连接数据库
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='k1', passwd='123', db='db10', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select s.id,stu_name,c.class from student s left join class c on s.class_id =c.id")
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    return render(request,'student.html',{'result':result})

