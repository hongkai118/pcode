# -*- coding:utf-8 -*-
"""
作者：KYLE
日期：2021年06月12日
"""
import time
import pymysql
from django.shortcuts import HttpResponse, redirect, render

def mysql_select_all(sql_select,args):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='k1', passwd='123', db='db20', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql_select,args)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def mysql_select_one(sql_select,args):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='k1', passwd='123', db='db20', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql_select,args)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def mysql_modify(sql_select,args):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='k1', passwd='123', db='db20', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql_select,args)
    conn.commit()
    cursor.close()
    conn.close()

def test(request):
    return HttpResponse('ADFADF')




def zoffer(request):
    sql ='''
    select zoffer.id,hangye.hy_name,zhineng.zn_name,bumen.bm_name,company,title,cnd_name,
    offer_time,client_offer,team_offer,client_owner,offer_owner,contact_window,
    kyle,shelley,raya,amy,vera,skye,cristina,insert_time
    from zoffer 
    left join hangye on hangye.id=zoffer.hangye_id
    left join zhineng on zhineng.id=zoffer.zhineng_id
    left join bumen on bumen.id=zoffer.bumen_id
    '''
    result = mysql_select_all(sql,[])
    print(result)


    return render(request,'zoffer.html',{
        'result':result
    })

def cnd(request):
    sql="""
    select * 
    from cnd 
    left join hangye on hangye.id=cnd.hangye_id
    left join zhineng on zhineng.id=cnd.zhineng_id
    left join bumen on bumen.id=cnd.bumen_id
    left join jixing on jixing.id=cnd.jixing_id
    left join cnd_level on cnd_level.id=cnd.cnd_level
    order by cnd.id desc
    limit %s,50
    """
    page=0
    result = mysql_select_all(sql,[page,])

    for row in result[0:1]:
        print(row)

    return render(request,'cnd.html',{
        'result':result
    })

def add_cnd(request):
    if request.method=='GET':

        cnd_level = mysql_select_all('select * from cnd_level',[])
        hangye= mysql_select_all('select * from hangye', [])
        zhineng = mysql_select_all('select * from zhineng', [])
        bumen = mysql_select_all('select * from bumen', [])
        jixing = mysql_select_all('select * from jixing',[])

        insert_time = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))
        print(insert_time)

        return render(request, 'add_cnd.html', {
            'cnd_level':cnd_level,
            'hangye':hangye,
            'zhineng':zhineng,
            'bumen':bumen,
            'jixing':jixing
        })
    else:
        todo=request.POST.get('todo')
        motivation=request.POST.get('motivation')
        offer=request.POST.get('offer')
        cnd_level=request.POST.get('cnd_level')
        min_salary=request.POST.get('min_salary')
        max_salary=request.POST.get('max_salary')
        hangye_id=request.POST.get('hangye_id')
        zhineng_id=request.POST.get('zhineng_id')
        bumen_id=request.POST.get('bumen_id')
        jixing_id=request.POST.get('jixing_id')
        warning=request.POST.get('warning')
        board_time=request.POST.get('board_time')
        profile_url=request.POST.get('profile_url')
        company=request.POST.get('company')
        cnd_name=request.POST.get('cnd_name')
        c_name=request.POST.get('c_name')
        gender=request.POST.get('gender')
        degree=request.POST.get('degree')

        location = request.POST.get('location')
        title = request.POST.get('title')
        # birth_day = request.POST.get('birth_day')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        wechat = request.POST.get('wechat')
        cv = request.POST.get('cv')
        email_notice = request.POST.get('email_notice')
        expect_workplace = request.POST.get('expect_workplace')
        comments = request.POST.get('comments')
        consultant='kyle'
        insert_time=time.strftime('%Y-%m-%d %X',time.localtime(time.time()))


        # print('薪资范围:',min_salary,max_salary)

        #将以上数据插入数据库
        #没有学校，毕业时间和专业
        sql_add_cnd="""
        insert into cnd(todo,motivation,offer,cnd_level,min_salary,max_salary,
          hangye_id,zhineng_id,bumen_id,jixing_id,warning,board_time,profile_url,
          company,title,cnd_name,c_name,gender,location,
          phone,email,wechat,cv,email_notice,expect_workplace,consultant,comments,insert_time)
          values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)  
        """
        mysql_modify(sql_add_cnd,
                     [todo,motivation,offer,cnd_level,min_salary,max_salary,
          hangye_id,zhineng_id,bumen_id,jixing_id,warning,board_time,profile_url,
          company,title,cnd_name,c_name,gender,location,
          phone,email,wechat,cv,email_notice,expect_workplace,consultant,comments,insert_time]
                     )

        return redirect('/cnd/')


