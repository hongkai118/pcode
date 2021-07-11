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

    if request.method=='GET':
        s_time ='2020-2-1'
        e_time ='2021-1-31'

    else:
        s_time=request.POST.get('s_time')
        e_time=request.POST.get('e_time')

    #获取每个顾问每月的offer情况
    # sql = """select DATE_FORMAT(offer_time,'%%Y-%%m') mon,
    # sum(if(yg_name='kyle',yg_yeji,0)) 'kyle',
    # sum(if(yg_name='shelley',yg_yeji,0)) 'shelley',
    # sum(if(yg_name='raya',yg_yeji,0)) 'raya',
    # sum(if(yg_name='vera',yg_yeji,0)) 'vera',
    # sum(if(yg_name='amy',yg_yeji,0)) 'amy',
    # sum(if(yg_name='skye',yg_yeji,0)) 'skye',
    # sum(if(yg_name='cristina',yg_yeji,0)) 'cristina'
    #
    # from zoffer left join ygoffer on offer_id=zoffer.id
    # WHERE offer_TIME BETWEEN %s AND %s
    # GROUP BY mon
    # ORDER BY mon asc"""
    sql="""select DATE_FORMAT(offer_time,'%%Y-%%m') mon,sum(kyle) kyle,sum(shelley) shelley,sum(raya) raya,
    sum(vera) vera,sum(amy) amy,sum(skye) skye,sum(cristina) cristina
    from guwen_month_offer where offer_time between %s and %s
    GROUP BY mon
    ORDER BY mon asc
    """
    result = mysql_select_all(sql, [s_time, e_time])

    #获取每月的Team_offer情况，只能通过zoffer单表来获取。不能连表来获取，因为连表后team_offer字段会重复。
    sql_teamoffer = """select DATE_FORMAT(offer_time,'%%Y-%%m') mon,sum(team_offer) team_performance from zoffer
        WHERE offer_time BETWEEN %s AND %s
        GROUP BY mon
        ORDER BY mon asc"""
    team_offers = mysql_select_all(sql_teamoffer,[s_time, e_time])

    #将团队业绩和员工业绩组合到一个字典里
    for i in range(len(result)):
        result[i]['team_performance'] = team_offers[i]['team_performance']
        # print(result[i])

    #获取各成员offer综合
    # sql_ygsum = """select yg_name,sum(yg_yeji) yeji
    #     from ygoffer left join zoffer on offer_id=zoffer.id
    #
    #     WHERE offer_time BETWEEN %s AND %s
    #     GROUP BY yg_name
    #     """
    # ygsum = mysql_select_all(sql_ygsum, [s_time, e_time])
    # print(ygsum)


    #团队总业绩
    sum_team_sql="""
    select sum(team_offer) team_offer from zoffer WHERE offer_time BETWEEN %s AND %s
    """
    sum_team_offer = mysql_select_one(sum_team_sql, [s_time, e_time])
    # print(sum_team_offer)

    #员工总业绩
    sum_guwen_sql="""
    select sum(kyle) kyle, sum(shelley) shelley, sum(raya) raya, sum(vera) vera, sum(amy) amy, sum(skye) skye, sum(cristina) cristina
    from guwen_month_offer
    where offer_time between %s and %s 
    """
    sum_guwen_offer = mysql_select_one(sum_guwen_sql, [s_time, e_time])
    # print(sum_guwen_offer)

    #团队和员工总计也组合一下
    sum_guwen_offer['team_offer']=sum_team_offer['team_offer']

    ####
    ####
    #offer个数,团队总offer个数
    sql_count_all="""
    select count(offer_owner) count_all from zoffer
    where offer_owner in('raya','shelley','kyle','vera','amy','cristina','skye')
    and offer_time BETWEEN %s and %s
    """
    count_all=mysql_select_one(sql_count_all, [s_time, e_time])

    #顾问的offer个数
    sql_count_consultant="""
    select offer_owner,count(offer_owner) count_offer from zoffer
    where offer_time BETWEEN %s and %s 
    GROUP BY offer_owner
    """
    count_consultant = mysql_select_all(sql_count_consultant, [s_time, e_time])

       #重新构造一下将list变为字典
    count_cons={}
    count_cons['team_offer'] = count_all['count_all']
    for c_row in count_consultant:
        count_cons[c_row['offer_owner']] = c_row['count_offer']

       #填充一下各顾问没有offer时，没有值的情况
    try:
        count_cons['team_offer']
    except:
        count_cons['team_offer']=0
    try:
        count_cons['kyle']
    except:
        count_cons['kyle'] = 0
    try:
        count_cons['shelley']
    except:
        count_cons['shelley'] = 0
    try:
        count_cons['raya']
    except:
        count_cons['raya'] = 0
    try:
        count_cons['vera']
    except:
        count_cons['vera'] = 0
    try:
        count_cons['amy']
    except:
        count_cons['amy'] = 0
    try:
        count_cons['skye']
    except:
        count_cons['skye'] = 0
    try:
        count_cons['cristina']
    except:
        count_cons['cristina'] = 0




                            # 计算平均数
    avg_offer={}
    print(sum_guwen_offer)
    print(count_cons)

    for key, value in sum_guwen_offer.items():
        try:
            avg_offer[key] = round(value/count_cons[key],0) #保留0位小数
        except:
            avg_offer[key] ='0'
    print(avg_offer)




    return render(request, 'month_offer.html', {"result": result,
                                                'sum_guwen_offer': sum_guwen_offer,
                                                's_time': s_time,
                                                'e_time': e_time,
                                                'count_cons':count_cons,
                                                'avg_offer':avg_offer
                                                })



def client_value(request):

    if request.method=='GET':
        s_time ='2020-2-1'
        e_time ='2021-1-30'

    else:
        s_time=request.POST.get('s_time')
        e_time=request.POST.get('e_time')

    # 获得客户名字，offer业绩，offer个数入
    sql = """
    select company,sum(client_offer) offer,sum(team_offer) sum_team_offer,count(client_offer) jishu from zoffer
    where offer_time between %s and %s
    GROUP BY company
    ORDER BY sum(client_offer) desc
    """
    result = mysql_select_all(sql, [s_time,e_time])

    #给result添加，一个编号栏
    num = 1
    for i in range(len(result)):
        result[i]['num']=num
        num=num+1

    #所有客户的总业绩
    sum_client_sql="""
    select sum(client_offer) client_sum_offer,sum(team_offer) sum_team_offer,count(client_offer) offer_counts from zoffer
    where offer_time between %s and %s
    """
    client_offer = mysql_select_one(sum_client_sql, [s_time,e_time])

    ########################
    #再建立一个表格，用来获取，各顾问Owner的对团队的贡献
    #
    sql_sum_owner = """
    select client_owner,sum(team_offer) team_offer
    from zoffer
    where offer_time BETWEEN %s and %s
    GROUP BY client_owner
    """
    sum_owner=mysql_select_all(sql_sum_owner,[s_time,e_time])
    # sum_owner_dict={}
    # for row_owner in sum_owner:
    #     sum_owner_dict[row_owner['client_owner']]= row_owner['team_offer']
    # print(sum_owner_dict)



    return render(request, 'client_value.html', {
        "result": result,
        'client_offer':client_offer,
        's_time':s_time,
        'e_time':e_time,
        'sum_owner':sum_owner

        })

