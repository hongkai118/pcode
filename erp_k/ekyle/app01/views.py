# -*- coding:utf-8 -*-
"""
作者：KYLE
日期：2021年06月05日
"""
from django.shortcuts import HttpResponse, render, redirect
import pymysql
import time

def mysql_select_all(sql_select,args):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='k1', passwd='123', db='db10', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql_select,args)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def mysql_select_one(sql_select,args):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='k1', passwd='123', db='db10', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql_select,args)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def mysql_modify(sql_select,args):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='k1', passwd='123', db='db10', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql_select,args)
    conn.commit()
    cursor.close()
    conn.close()

def login(request):
    return render(request,'login.html')


def zoffer(request):
    sql ='''
    select zoffer.id,hangye.hy_name,zhineng.zn_name,bumen.bm_name,cnd_name,company,title,client_offer,team_offer,client_owner,offer_time,contact_window,offer_owner,insert_time
    from zoffer 
    left join hangye on hangye.id=zoffer.hangye_id
    left join zhineng on zhineng.id=zoffer.zhineng_id
    left join bumen on bumen.id=zoffer.bumen_id
    '''
    offer_list=mysql_select_all(sql,[])

    for i in range(len(offer_list)):
        offer_list[i]['offer_time']=str(offer_list[i]['offer_time'])

    print(offer_list[0])
    return render(request,'zoffer.html',{'offer_list':offer_list})

def add_offer(request):
    if request.method =='GET':
        hangye_list=mysql_select_all('select * from hangye',[])
        zhineng_list=mysql_select_all('select * from zhineng',[])
        bumen_list=mysql_select_all('select * from bumen', [])
        return render(request, 'add_offer.html',{
            'hangye_list':hangye_list,
            'zhineng_list':zhineng_list,
            'bumen_list':bumen_list
        })

    else:
        hangye_id=request.POST.get('hangye_id')
        zhineng_id=request.POST.get('zhineng_id')
        bumen_id=request.POST.get('bumen_id')
        company=request.POST.get('company')
        title=request.POST.get('title')
        cnd_name=request.POST.get('cnd_name')
        client_offer=request.POST.get('client_offer')
        team_offer=request.POST.get('team_offer')
        offer_time=request.POST.get('offer_time')
        client_owner=request.POST.get('client_owner')
        contact_window=request.POST.get('contact_window')
        offer_owner=request.POST.get('offer_owner')
        # insert_time=time.strftime('%Y-%m-%d %X',time.localtime(time.time()))

        sql = '''
        insert into zoffer(hangye_id, zhineng_id,bumen_id,company,title,cnd_name,client_offer,team_offer,offer_time
        ,client_owner,contact_window,offer_owner,insert_time) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,now())
        '''
        args=[hangye_id,zhineng_id,bumen_id,company,title,cnd_name,client_offer,team_offer,offer_time,client_owner,contact_window,
              offer_owner]
        mysql_modify(sql,args)

        return redirect('/zoffer/')

def edit_offer(request):
    if request.method == 'GET':
        id=request.GET.get('id')
        sql="""
        select id,hangye_id,zhineng_id,bumen_id,cnd_name,company,title,client_offer,team_offer,client_owner,offer_time,contact_window,offer_owner
        from zoffer 
        where zoffer.id =%s 
        """
        current_offer=mysql_select_one(sql,[id,])
        print(current_offer)

        hangye_list = mysql_select_all('select * from hangye', [])
        zhineng_list = mysql_select_all('select * from zhineng', [])
        bumen_list = mysql_select_all('select * from bumen', [])

        return render(request,'edit_offer.html',{
            'current_offer':current_offer,
            'hangye_list':hangye_list,
            'zhineng_list':zhineng_list,
            'bumen_list':bumen_list
        })
    else:
        id = request.GET.get('id')
        hangye_id=request.POST.get('hangye_id')
        zhineng_id=request.POST.get('zhineng_id')
        bumen_id=request.POST.get('bumen_id')
        company=request.POST.get('company')
        title=request.POST.get('title')
        cnd_name=request.POST.get('cnd_name')
        client_offer=request.POST.get('client_offer')
        team_offer=request.POST.get('team_offer')
        # offer_time=request.POST.get('offer_time')
        client_owner=request.POST.get('client_owner')
        contact_window=request.POST.get('contact_window')
        offer_owner=request.POST.get('offer_owner')

        sql = '''
        update zoffer set 
        hangye_id=%s, 
        zhineng_id=%s,
        bumen_id=%s,
        company=%s,
        title=%s,
        cnd_name=%s,
        client_offer=%s,
        team_offer=%s,
        client_owner=%s,
        contact_window=%s,
        offer_owner=%s,
        insert_time=now()
        where id = %s
        '''
        args=[hangye_id,zhineng_id,bumen_id,company,title,cnd_name,client_offer,team_offer,client_owner,contact_window,
              offer_owner,id]
        mysql_modify(sql,args)
        return redirect('/zoffer/')


def month_offer(request):
    sql = """
    select offer_time,sum(team_offer) month_offer from zoffer
    group by offer_time
    order by offer_time asc
    """
    result = mysql_select_all(sql, [])
    print(result)
    for i in range(len(result)):
        result[i]['offer_time']=str(result[i]['offer_time'])


        # print(i['offer_time'].strftime('%Y-%m-%d'))
    sumoffer = mysql_select_one('select sum(team_offer) team_offer from zoffer',[])


    return render(request, 'month_offer.html', {"result": result, 'sumoffer': sumoffer})


def client_value(request):
    sql = """
    select company, sum(client_offer) offer,count(client_offer) jishu from zoffer
    GROUP BY company
    ORDER BY sum(client_offer) desc
    """
    result = mysql_select_all(sql, [])
    client_offer = mysql_select_one('select sum(client_offer) client_sum_offer from zoffer', [])
    return render(request, 'client_value.html', {"result": result,'client_offer':client_offer})
