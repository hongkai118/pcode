#待更新内容
#更新1：
#1）sleep时间设置为5-10秒time.sleep(random.randint(5,10))

#更新2：2020.12.26
#1）防止一次没有爬完就中断：增加可选择页面

#更新3：2021.1.16
# 增加密码输入变为星号
# Linkedin页面xpath路径改变，重新写代码定位。

#更新4：2021-4-27
#xpath搜索不出内容时，很可能是因为，自己在网页上看到的xpath路径，与下载web页面后的路径不一致。遇到这种情况，通过 with open('xxx') 下载文件，浏览器打开查看。

#selenium
#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36

#chrome
#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36


from selenium import webdriver
from lxml import etree
import time
import xlwings as xw
import json
import sys
import requests
import smtplib
import random
import msvcrt

# 实例化浏览器对象
opt = webdriver.ChromeOptions()
opt.add_argument('--disable-gpu')  # 禁止GPU渲染
# opt.add_argument('--headless')  # 无界面模式
#opt.add_argument('user-agent="Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"') #更换头部
# 1.设置为开发者模式，防止被各大网站识别使用了selenium;2.禁止打印日志
opt.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=opt)

#全局变量，打开excel, 制作表头
print('打开my_linkedin.xlsx文件')
try:
    wb = xw.Book("my_linkedin.xlsx")

except:
    wb = xw.Book()

sht = wb.sheets["sheet1"]
biaotou = ['任职时间','Profile','pro_url','公司','姓名','简称','学历','地点','职位','毕业时间','专业','学校','年龄','电话','邮箱','微信']
# biaotou = ['Profile','姓名','任职时间','公司','职位','地点','毕业时间','学历','专业','学校','电话','邮箱','微信']
sht.range('A1').value = biaotou


def pwd_input(text):
    """
    输入信息加密
    """
    print(text,end='',flush=True)
    chars = []
    while True:
        try:
            newChar = msvcrt.getch().decode(encoding="utf-8")
        except:
            return input("你很可能不是在cmd命令行下运行，密码输入将不能隐藏:")
        # 换行 -- 输入结束
        if newChar in '\r\n': 
             break
        # 如果是退格，则删除密码末尾一位并且删除一个星号
        elif newChar == '\b': # 如果是退格，则删除密码末尾一位并且删除一个星号
             if chars:
                 del chars[-1]
                 # 光标回退一格
                 msvcrt.putch('\b'.encode(encoding='utf-8')) 
                 # 输出一个空格覆盖原来的星号
                 msvcrt.putch( ' '.encode(encoding='utf-8')) 
                 # 光标回退一格准备接受新的输入
                 msvcrt.putch('\b'.encode(encoding='utf-8')) 
        else:
            chars.append(newChar)
            # 命令行中显示为星号
            msvcrt.putch('*'.encode(encoding='utf-8')) 
    # 返回真实信息
    return ''.join(chars)

# 将读取cookies文件，登录linkedin
def login_linkedin():
    driver.get('https://www.linkedin.com/feed/')
    driver.delete_all_cookies()
    with open('link_cookies.json', 'r', encoding='utf-8') as f:
        listCookies = json.loads(f.read())
    for cookie in listCookies:
        driver.add_cookie({
            'domain': '.linkedin.com',
            'name': cookie['name'],
            'value': cookie['value'],
            'path': '/',
            'expires': None
        })


def get_name_list(url,page_num=1):

    #这个部分点击按钮Connections
    try:
        int(page_num)
    except:
        print('注意：下载页码用1，2，3数字，不能用字符和中文!')
        sys.exit(0)
    url = url+'&page={}'
    counts_name = 10
#    page_num = 0  # 给page计数
    excel_row = 2  # 行标
    if page_num=='0':
        page_num=1

    while counts_name == 10:
        name_list = []  # 用来存储每一页的候选人数据,翻页后清空。
        
        s_url = url.format(page_num)
        driver.get(url=s_url)
        driver.implicitly_wait(3)
        time.sleep(5)
        
        # #点击手动操作
        # driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div[1]/section/div/nav/div/div[1]/div/div[2]/ul/li[3]/div/span/button').click()
        
        #卡住，手动输入操作完成后，再进行一下操作
        input('是否操作完成(y)：',)

        html = driver.page_source
        tree = etree.HTML(html)

        name_temp = tree.xpath(
            '/html/body//div[3]/div/div[1]/div/div//div/div[2]/ul/li')
            #/html/body//div[3]/div/div[1]/div/div/main/div/div/div[2]/ul
            #/html/body/div[8]/div[3]/div/div[1]/div/div/main/div/div/div[2]/ul
        # print('-----------------------------------------------------------name_temp',len(name_temp))
        counts_name=len(name_temp)
        cnd_number = 0  # 给候选人计数

        for na in name_temp:
            cnd_number = cnd_number+1
            print('第{}页，第{}位候选人的信息:'.format(page_num, cnd_number))
            name = na.xpath('.//a/span/span[1]/text()')[0]
            profile_url = na.xpath('.//a/@href')[0]
            profile_url = profile_url.split('?')[0]
            contact_url = profile_url+'/detail/contact-info/'
            print(cnd_number, name, profile_url, contact_url)

            # 获得detail_info
            detail_list = get_detail_info(url=profile_url)
            contact_list = get_contact_info(url=contact_url)

            zuhe = detail_list+contact_list
            name_list.append(zuhe)
            print('')
        

        print('第{}页的{}候选人写入EXCEL。'.format(page_num, len(name_temp)))
        print('')
        excel_location = 'A'+str(excel_row)
        sht.range(excel_location).value = name_list
        excel_row = excel_row + len(name_temp)  # 行标每次移动候选人个人那么多行
        page_num = int(page_num)+1
        time.sleep(random.randint(3,8))

    print('本次共计{}位候选人'.format(excel_row-2))


# 获得获选人联系方式
def get_contact_info(url):

    driver.get(url)
    driver.implicitly_wait(3)
    time.sleep(2)    #必须设置sleep, implicitly 不怎么顶用。
    html = driver.page_source
    tree = etree.HTML(html)
    

    #xpath不到信息的时候，通过下载网页来看看检查，是否读取。
    # with open('contact.html','w',encoding='utf-8') as f:
    #     f.write(html)

    try:
        cnd_phone = tree.xpath(
            '/html/body/div[3]/div/div/div[2]/section/div/div[1]/div/section[2]/ul/li/span[1]/text() | /html/body/div[3]/div/div/div[2]/section/div/div[1]/div/section[3]/ul/li/span[1]/text()')[0].strip()
    except:
        cnd_phone = 'null'

    try:
        cnd_email = tree.xpath(
            '/html/body/div[3]/div/div/div[2]/section/div/div[1]/div/section[2]/div/a/text() | /html/body/div[3]/div/div/div[2]/section/div/div[1]/div/section[3]/div/a/text() | /html/body/div[3]/div/div/div[2]/section/div/div[1]/div/section[5]/div/a/text()')[0].strip()
        
        if '@' not in cnd_email:
            try:
                cnd_email = tree.xpath(
                    '/html/body/div[3]/div/div/div[2]/section/div/div[1]/div/section[4]/div/a/text()')[0].strip()
            except:
                cnd_email = 'null'
    except:
        cnd_email = 'null'

    try:
        we_chat = 'https://www.linkedin.com' + tree.xpath('/html/body/div[3]/div/div/div[2]/section/div/div[2]/div/div/section/div/a/@href')[0]
    except:
        we_chat = 'null'

    contact_list = [cnd_phone, cnd_email, we_chat]
    print('联系方式：', cnd_phone, cnd_email, we_chat)
    time.sleep(random.randint(3,8))

    return contact_list


# 获得候选人profile里面的信息
def get_detail_info(url):

    driver.get(url)
    driver.implicitly_wait(3)
    time.sleep(2)

    s_page = True  # 鼠标还没有滚动时的初始页面
    e_page = None  # 存储鼠标滚动后的页面

    y = 0  # 鼠标坐标
    n = 0  # 鼠标滚动次数

    # 如果滚轮滑倒底部,则前后两次页面源代码一直，则退出，以滑倒底部的页面源代码为准。
    # 注意：试国用window.srcollto(0,document.body.srocllheight)直接到底部，不行。很多数据无法加载。
    while s_page != e_page:
        s_page = e_page  # 第一次循环
        n = n+1
        y = y+1000
        driver.execute_script('window.scrollTo(0,{})'.format(y))
        driver.implicitly_wait(3)
        e_page = driver.page_source
        # print('滑动次数：',n)
    html = e_page
    
    #xpath无效时，用下载下来的网页，检查网页是否加载成功。
    # with open('hhhh.html','w',encoding='utf-8') as f:
    #     f.write(html)

    cnd_tree = etree.HTML(html)

    # 获取候选人相关信息
    try:

        cnd_name = cnd_tree.xpath(
                '/html/body/div[8]/div[3]/div//main/div/div[1]/section/div[2]/div[2]/div[1]/ul[1]/li[1]/text() | /html/body/div[7]/div[3]/div/div/div/div/div[2]/div/div/main/div/div[1]/section/div[2]/div[2]/div[1]/ul[1]/li[1]/text() | /html/body/div[6]/div[3]/div/div/div/div/div[2]/div/div/main/div/div[1]/section/div[2]/div[2]/div[1]/ul[1]/li[1]/text()')[0].strip()
    except:
        cnd_name = 'null'                                                                                                    

        #/html/body/div[8]/div[3]/div//main/div/div[1]/section/div[2]/div[2]/div[1]/ul[1]/li[1]
        #/html/body/div[8]/div[3]/div/div/div/div/div[2]/div/div/main/div/div[1]/section/div[2]/div[2]/div[1]/ul[1]/li[1]
    print('cnd_name:',cnd_name)
        #/html/body/div[7]/div[3]/div/div/div/div/div[2]/div/main/div/section/div[2]/div[2]/div[1]/ul[1]/li[1]
#    cnd_company=cnd_tree.xpath('/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[1]/h2/text()')[0].strip()
    # 注意，以下很多内容，全部都用了//,要修改时不要直接复制浏览器xpath路径
    # 工作经历
    try:                               
        cnd_company = cnd_tree.xpath('/html/body/div[7]/div[3]/div/div/div/div/div[2]/div/div/main/div/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/p[2]/text() |/html/body/div[6]/div[3]/div/div/div/div/div[2]/div/div/main/div/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/p[2]/text()')[0].strip()
    except:
        try:
            cnd_company = cnd_tree.xpath(
                '/html/body/div[7]/div[3]/div/div/div/div/div[2]//span/div/section/div[1]/section/ul/li[1]/section/div/a/div/div[2]/h3/span[2]/text() | /html/body/div[6]/div[3]/div/div/div/div/div[2]/div/div/main/div/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/p[2]/text()')[0].strip()
        except:
            cnd_company = 'null'
    print('cnd_company:',cnd_company)

    try:
        cnd_location = cnd_tree.xpath(
            '/html/body/div[7]/div[3]/div/div/div/div/div[2]//div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/h4/span[2]/text() | /html/body/div[6]/div[3]/div/div/div/div/div[2]//div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/h4/span[2]/text()')[0]
            #/html/body/div[7]/div[3]/div/div/div/div/div[2]///div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/h4/span[2]
    except:
        try:
            cnd_location = cnd_tree.xpath(
                '/html/body/div[7]/div[3]/div/div/div/div/div[2]//div[5]/span/div/section/div[2]/div[2]/div[1]/ul[2]/li[1]/text() | /html/body/div[6]/div[3]/div/div/div/div/div[2]//div[5]/span/div/section/div[2]/div[2]/div[1]/ul[2]/li[1]/text()')[0].strip()
        except:
            cnd_location = 'null'
    print('location:',cnd_location)

    try:
        cnd_time = cnd_tree.xpath(
            '/html/body/div[7]/div[3]/div/div/div/div/div[2]//div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/div/h4[1]/span[2]/text() | /html/body/div[6]/div[3]/div/div/div/div/div[2]//div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/div/h4[1]/span[2]/text()')[0]
    except:
        try:
            cnd_time = cnd_tree.xpath(
                '/html/body/div[7]/div[3]/div/div/div/div/div[2]//div[5]/span/div/section/div[1]/section/ul/li[1]/section/ul/li[1]/div/div/div/div/div/div/div/h4[1]/span[2]/text() | /html/body/div[6]/div[3]/div/div/div/div/div[2]//div[5]/span/div/section/div[1]/section/ul/li[1]/section/ul/li[1]/div/div/div/div/div/div/div/h4[1]/span[2]/text()')[0]
        except:
            cnd_time = 'null'
    
    print('cnd_time:',cnd_time)

    try:
        cnd_title = cnd_tree.xpath(
            '/html/body/div[7]/div[3]/div/div/div/div/div[2]//div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/h3/text() | /html/body/div[6]/div[3]/div/div/div/div/div[2]//div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/h3/text()')[0]
    except:
        try:
            cnd_title = cnd_tree.xpath(
                '/html/body/div[7]/div[3]/div/div/div/div/div[2]//div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/a/div/div[2]/h3/span[2]/text() | /html/body/div[6]/div[3]/div/div/div/div/div[2]//div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/a/div/div[2]/h3/span[2]/text()')[0]
            if cnd_title == cnd_company:  # 确实相等
                cnd_title = cnd_tree.xpath(
                    '/html/body/div[7]/div[3]/div/div/div/div/div[2]//div[5]/span/div/section/div[1]/section/ul/li[1]/section/ul/li[1]/div/div/div/div/div/div[1]/h3/span[2]/text() | /html/body/div[6]/div[3]/div/div/div/div/div[2]//div[5]/span/div/section/div[1]/section/ul/li[1]/section/ul/li[1]/div/div/div/div/div/div[1]/h3/span[2]/text()')[0]

        except:
            cnd_title = 'null'
    print('cnd_title:',cnd_title)

    # 教育信息
    try:  # 学校
        cnd_school = cnd_tree.xpath(
            '/html/body/div[7]/div[3]/div/div/div/div/div[2]//div[5]/span/div/section/div[2]/section/ul/li[1]/div/div/a/div[2]/div/h3/text() | /html/body/div[6]/div[3]/div/div/div/div/div[2]//div[5]/span/div/section/div[2]/section/ul/li[1]/div/div/a/div[2]/div/h3/text()')[0]
    except:
        cnd_school = 'null'
    print('cnd_school:',cnd_school)

    try:  # 学历
        cnd_degree = cnd_tree.xpath(
            '/html/body/div[7]/div[3]/div/div/div/div/div[2]//div[5]/span/div/section/div[2]/section/ul/li[1]/div/div/a/div[2]/div/p[1]/span[2]/text() | /html/body/div[6]/div[3]/div/div/div/div/div[2]//div[5]/span/div/section/div[2]/section/ul/li[1]/div/div/a/div[2]/div/p[1]/span[2]/text()')[0]
    except:
        cnd_degree = 'null'
    
    print('cnd_degree:',cnd_degree)
    try:  # 专业
        cnd_major = cnd_tree.xpath(
            '/html/body/div[7]/div[3]/div/div/div/div/div[2]//div[5]/span/div/section/div[2]/section/ul/li[1]/div/div/a/div[2]/div/p[2]/span[2]/text() | /html/body/div[6]/div[3]/div/div/div/div/div[2]//div[5]/span/div/section/div[2]/section/ul/li[1]/div/div/a/div[2]/div/p[2]/span[2]/text()')[0]
    except:
        cnd_major = 'null'
    print('cnd_major:',cnd_major)
    try:  # 毕业时间
        cnd_edu_time = cnd_tree.xpath(
            '/html/body/div[7]/div[3]/div/div/div/div/div[2]//div[5]/span/div/section/div[2]/section/ul/li[1]/div/div/a/div[2]/p/span[2]/time[2]/text() | /html/body/div[6]/div[3]/div/div/div/div/div[2]//div[5]/span/div/section/div[2]/section/ul/li[1]/div/div/a/div[2]/p/span[2]/time[2]/text()')[0]
    except:
        cnd_edu_time = 'null'

    print('cnd_edu_time:',cnd_edu_time)

    print(cnd_name, cnd_time, cnd_title, cnd_company, cnd_location)
    print(cnd_edu_time, cnd_degree, cnd_major, cnd_school)
    cnd_short_name=''
    cnd_age=''
    p_url=''

#biaotou = ['任职时间','Profile','pro_url','公司','姓名','简称','学历','地点','职位','毕业时间','专业','学校','年龄','电话','邮箱','微信']

    detail_list = [cnd_time,p_url,url,cnd_company, cnd_name,cnd_short_name,cnd_degree,cnd_location,cnd_title,
                     cnd_edu_time, cnd_major, cnd_school,cnd_age]
    time.sleep(random.randint(3,8))
    return detail_list




#检测内容：1. 从公司离职后失效(公司邮箱登录）2. 非团队成员失效（团队list)

def check_permission():
    KyleTeam=['kyle.you','shelley.xie','steven.gou','raya.zhang','vera.wu','amy.dai','rachel.ling','kevin.lee']
    print('进行身份验证....')
    sender = input('公司邮箱：')
    auth_pwd= pwd_input('邮箱密码：')
    print('')
    

    try:
        email_type=sender.split("@")[1]
    except:
        print('邮箱格式不对..')
        sys.exit(0)

    if sender.split('@')[0] not in KyleTeam:
        print('未授权的用户..\n')
        sys.exit(0)

    if 'kenneth' not in email_type:
        print("只支持公司邮箱...退出")
        sys.exit(0)

    #实例化邮箱，连接邮箱服务器
    smtp = smtplib.SMTP()
    smtp.connect('smtp.263.net')

    #登录测试
    try:
        smtp.login(sender,auth_pwd)
        print('**成功通过身份验证,欢迎使用**\n')
    except:
        print("用户名或密码错误,请重新运行.....")
        smtp.close()
        sys.exit(0)

def inputDefault(statement,default):
    text = input(statement)
    if text == "": 
        text = str(default)
    return text

if __name__=='__main__':
    print('版本：3.3')
    print('更新时间：2021-4-23')
    print('--------------------------------------------\n')
    # check_permission()
    input_url = input('请输入搜索页面:')
    page_num=inputDefault('请选在从第几页开始（默认从第1页开始）：',1)
    # input_url='https://www.linkedin.com/search/results/people/?keywords=amgen'
    # page_num=1

    
    try:
        print('请等待，正在登录网站.....')
        login_linkedin()  # 登录通过cookies直接登录linkedin
        print('登录完成')
    except:
        print('登录不成功,确保link_cookies.json文件在当前目录下')
        sys.exit(0)

    print('请耐心等待，正在解析网页........')
    get_name_list(url=input_url,page_num=page_num)  # 为了一边解析，一边将数据导入excel，将detail和contact都套进这个函数。

    driver.quit()