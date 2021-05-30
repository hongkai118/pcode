import pymysql


def get_list(sql_select, args):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='k1', passwd='123', db='db10', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql_select, args)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def modify(sql_modify,args):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='k1', passwd='123', db='db10', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql_modify, args)
    conn.commit()
    cursor.close()
    conn.close()

def get_one(sql_select, args):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='k1', passwd='123', db='db10', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql_select, args)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result