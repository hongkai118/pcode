# 基金经理页管理的基金
#jijin6:更新时间2020.1.10
#1. 增加基金经理筛选页
#2. 解决list数据过多时，无法加入空串的而卡死的问题

#jijin7_jiancha,用来检查自己购买的基金的规模，持有人情况等等


from selenium import webdriver
from lxml import etree
import time
import xlwings as xw
import re

#实例化一个浏览器对象
opt = webdriver.ChromeOptions()
opt.add_argument('--disable-gpu') #禁止GPU渲染
opt.add_argument('--headless') #无界面模式
#1.设置为开发者模式，防止被各大网站识别使用了selenium;2.禁止打印日志
opt.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=opt)

def get_ranking_code(url):
    driver.get(url=url)
    driver.implicitly_wait(3) #隐形等待，有结果时立即执行
    html = driver.page_source

    tree = etree.HTML(html)
    code_temp=tree.xpath('//*[@id="dbtable"]/tbody/tr') #获取基金代码列表
    
    code_list=[]
    for code in code_temp:
        code_num = code.xpath('./td[3]/a//text()')[0]
        code_list.append(code_num)
    return code_list

#
#//*[@id="jj"]/p/a
def get_search_code(url):
    driver.get(url=url)
    driver.implicitly_wait(3) #隐形等待，有结果时立即执行
    
    html_temp=driver.page_source
    tree_temp = etree.HTML(html_temp)

    #判断点击按钮是否为空
    gengduo=tree_temp.xpath('//*[@id="jj"]/p/a')
    if gengduo == []:
        tree=tree_temp

    else:
        #点击展开更多基金
        more_jj=driver.find_element_by_xpath('//*[@id="jj"]/p/a')
        more_jj.click()
        time.sleep(3)
        html = driver.page_source
        tree = etree.HTML(html)
        print("展开所有基金....")

#    tree = etree.HTML(html)
    code_table1=tree.xpath('//*[@id="jj"]/div[2]/table[1]/tbody/tr') #获取基金代码列表
    code_table2=tree.xpath('//*[@id="jj"]/div[2]/table[2]/tbody/tr') #获取基金代码列表
    code_table3=tree.xpath('//*[@id="jj"]/div[2]/table[3]/tbody/tr') #获取基金代码列表

    code_list=[]
    #表一
    for code in code_table1:
        test_table1 = code.xpath('./td[1]/a//text()')
        if test_table1 != []:
            code_num = code.xpath('./td[1]/a//text()')[0]
            if len(code_num) !=6:
                code_num = code.xpath('./td[1]/a//text()')[0]+code.xpath('./td[1]/a//text()')[1]
        
            print(code_num)
            code_list.append(code_num)
    
    #表二
    
    for code in code_table2:
        test_table2=code.xpath('./td[1]/a//text()')

        if test_table2 != []:
            code_num = code.xpath('./td[1]/a//text()')[0]
            if len(code_num) !=6:
                code_num = code.xpath('./td[1]/a//text()')[0]+code.xpath('./td[1]/a//text()')[1]
        
            print(code_num)
            code_list.append(code_num)

        
    #表三
    for code in code_table3:
        test_table3=code.xpath('./td[1]/a//text()')

        if test_table3 != []:
            code_num = code.xpath('./td[1]/a//text()')[0]
            if len(code_num) !=6:
                code_num = code.xpath('./td[1]/a//text()')[0]+code.xpath('./td[1]/a//text()')[1]
        
            print(code_num)
            code_list.append(code_num)

    print('共有{}支基金'.format(len(code_list)))
    return code_list

#获取基金经理管理的基金代码：
def get_manager_code(url):
    
    driver.get(url=url)
    driver.implicitly_wait(3) #隐形等待，有结果时立即执行
    html = driver.page_source

    tree = etree.HTML(html)
    code_temp=tree.xpath('/html/body/div[6]/div[2]/div[1]/table/tbody/tr') #获取基金代码列表
        
    code_list=[]
    for code in code_temp:
        code_num = code.xpath('./td/a/text()')[0]
        print(code_num)
        code_list.append(code_num)
    return code_list



def get_detail(code_list):
    all_jj=[]
    r_num =1 #记录行的位置
    jj_count =1
    for code in code_list:
        print('获取基金的详细情况:',code)
        print('构造基金主页，持有人机构，基本概况页面...')
        url_home = 'http://fund.eastmoney.com/'+code+'.html' #基金主页url构造
        url_cyrjg = 'http://fundf10.eastmoney.com/'+'cyrjg_'+code+'.html' #持有人结构url构造
        url_jbgk = 'http://fundf10.eastmoney.com/'+'jbgk_'+code+'.html' #基本概况url构造
    
        print('访问基金主页...')
        driver.get(url=url_home) #访问此基金主页
        driver.implicitly_wait(3) #隐形等待，有结果时立即执行
        html_home = driver.page_source
        html_t = etree.HTML(html_home)
        
        #检查误差是否为空
        if html_t.xpath('//*[@id="body"]/div[11]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[3]/td/text()[2]') !=[]:
            wucha = html_t.xpath('//*[@id="body"]/div[11]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[3]/td/text()[2]')[0]
        else:
            wucha ='Null'
    
        manager = html_t.xpath('//*[@id="fundManager"]/div[2]/ul/li[1]/div/div/div[2]/div[1]/a/text()')[0]
        m_time = html_t.xpath('//*[@id="fundManager"]/div[2]/ul/li[1]/div/div/div[2]/div[4]/text()')[0]
        fund_scale = html_t.xpath('//*[@id="fundManager"]/div[2]/ul/li[1]/div/div/div[2]/div[6]/text()')[0]
        late_year =html_t.xpath('//*[@id="increaseAmount_stage"]/table/tbody/tr[2]/td[7]/div/text()')[0]
        year2019=html_t.xpath('//*[@id="IncreaseAmount"]/div[2]/ul/li[3]/table/tbody/tr[2]/td[2]/div/text()')[0]
        year2018=html_t.xpath('//*[@id="IncreaseAmount"]/div[2]/ul/li[3]/table/tbody/tr[2]/td[3]/div/text()')[0]
        year2017=html_t.xpath('//*[@id="IncreaseAmount"]/div[2]/ul/li[3]/table/tbody/tr[2]/td[4]/div/text()')[0]
        year2016=html_t.xpath('//*[@id="IncreaseAmount"]/div[2]/ul/li[3]/table/tbody/tr[2]/td[5]/div/text()')[0]
        year2015=html_t.xpath('//*[@id="IncreaseAmount"]/div[2]/ul/li[3]/table/tbody/tr[2]/td[6]/div/text()')[0]
        year2014=html_t.xpath('//*[@id="IncreaseAmount"]/div[2]/ul/li[3]/table/tbody/tr[2]/td[7]/div/text()')[0]

        # jjpj_temp=html_t.xpath('//*[@id="body"]/div[11]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]/div/@class')[0]
        # if len(jjpj_temp) == 4:
        #     jjpj ='暂无评级'
        # else:
        #     jjpj = jjpj_temp[-1]

        print('访问持有人结构页....')
        driver.get(url=url_cyrjg)
        driver.implicitly_wait(3) #隐形等待，有结果时立即执行
        cyrjg_home =driver.page_source
        cyrjg=etree.HTML(cyrjg_home)
        if cyrjg.xpath('//*[@id="summary"]/text()[2]') !=[]:
            try:
                cyrjg_temp =cyrjg.xpath('//*[@id="summary"]/text()[2]')[0] #持有人结构信息
                cyrjg_info = re.findall(r'\d{1,3}\.\d{2}%',cyrjg_temp)[-1]
            except:
                cyrjg_info='Null'
        else:
            cyrjg_info ='Null'

        print('访问基本概况页....')
        driver.get(url=url_jbgk)
        driver.implicitly_wait(3) #隐形等待，有结果时立即执行
        jbgk_home =driver.page_source
        jbgk=etree.HTML(jbgk_home)

        try:
            jj_type = jbgk.xpath('//*[@id="bodydiv"]/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tbody/tr[2]/td[2]/text()')[0]
        except:
            jj_type='null'
        name = jbgk.xpath('//*[@id="bodydiv"]/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tbody/tr[1]/td[1]/text()')[0]
        jj_code=jbgk.xpath('//*[@id="bodydiv"]/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tbody/tr[2]/td[1]/text()')[0]
        start_day=jbgk.xpath('//*[@id="bodydiv"]/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tbody/tr[3]/td[2]/text()')[0][:11]
        guimo=jbgk.xpath('//*[@id="bodydiv"]/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tbody/tr[4]/td[1]/text()')[0][:-19]
        
        guanlifei =jbgk.xpath('//*[@id="bodydiv"]/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tbody/tr[7]/td[1]/text() | //*[@id="bodydiv"]/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tbody/tr[7]/td[1]/a')[0][:-4]
        if len(guanlifei) == 0:
            guanlifei='暂无信息'

        tuoguanfei = jbgk.xpath('//*[@id="bodydiv"]/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tbody/tr[7]/td[2]/text()')[0][:-4]
        fuwufei =jbgk.xpath('//*[@id="bodydiv"]/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tbody/tr[8]/td[1]/text()')[0][:-4]
    
        print('数据封装为列表...')
        zuhe=[name,jj_code,jj_type,start_day,guimo,manager,m_time,fund_scale,cyrjg_info,guanlifei,tuoguanfei,fuwufei,wucha,late_year,year2019,year2018,year2017,year2016,year2015,year2014]
#        all_jj.append(zuhe)

        r_num = r_num+1
        location='A'+str(r_num)
        sht.range(location).value=zuhe
        print('已保存到EXCEL:第{}支基金，代码：{}'.format(jj_count,jj_code))
        jj_count = jj_count+1

    
    print('已保存到Excel，共计{}支基金'.format(jj_count-1)) 

  
    driver.quit() 

if __name__=='__main__':
#直接找排行榜主页就可以，其中pn是指每页多少个基金，可自己更改
#指数搜索页面：例在主页的搜索框中，输入“上证50”-->点击下拉选项中选择"在基金主题分类下搜索上证50,得到的url
# http://fund.eastmoney.com/data/fundsearch.html?spm=search&key=%E4%B8%8A%E8%AF%8150#key%E4%B8%8A%E8%AF%8150;ztjj
#
# 排行榜页面：天天基金主页-->基金排行-->再进行相关筛选得到的页面
# http://fund.eastmoney.com/data/fundranking.html#tzq;c0;r;s3nzf;pn50;ddesc;qsd20191204;qed20201204;qdii;zq041;gg;gzbd053;gzfs052;bbzt;sfbb

# 基金经理管理的所有基金：
# http://fund.eastmoney.com/manager/30382736.html
# http://fund.eastmoney.com/manager/30066292.html


    # print('作者：Kyle')
    # print('发布时间：20200115')
    # print('-----------------------------------------------------------------------')
    # print('可识别三类URL:\n')
    # print('1. 指数搜索页面：例在主页的搜索框中，输入“上证50”-->点击下拉选项中选择"在基金主题分类下搜索上证50,得到的页面')
    # print('例如：http://fund.eastmoney.com/data/fundsearch.html?spm=search&key=%E4%B8%8A%E8%AF%8150#key%E4%B8%8A%E8%AF%8150;ztjj')
    # print('')
    # print('2. 排行榜页面：天天基金主页-->基金排行-->再进行相关筛选得到的页面')
    # print('例如: http://fund.eastmoney.com/data/fundranking.html#tzq;c0;r;s3nzf;pn50;ddesc;qsd20191204;qed20201204;qdii;zq041;gg;gzbd053;gzfs052;bbzt;sfbb')
    
    # print('')
    # print('3. 基金经理搜索页面：例在主页的搜索框中，输入“张三”-->点击下拉选项中选择"基金经理"-->进入新的页面-->选择“张三”-->跳转的主页')
    # print('例如：http://fund.eastmoney.com/manager/30066292.html')

    # start_page = input('请输入网页:')
    # # start_page = 'http://fund.eastmoney.com/manager/30066292.html'
    
    # website = start_page.split('/')[4]  #fundranking....或fundsearch.....


    print('打开excel并记录数据...')
    try:
        wb = xw.Book("jj_jiancha.xlsx")
    except:
        wb = xw.Book()
    sht = wb.sheets["sheet1"]

    biaotou = ['基金全名','代码','类型','成立日期','规模','经理','上岗','经理人管理总量','持有人','管理费','托管费','服务费','跟踪误差','最近1年','2020年','2019年','2018年','2017年','2016年','2015年']
    sht.range('A1').value = biaotou
    
    # if 'fundranking' in website:
    #     code_list=get_ranking_code(start_page)
    #     print(code_list)
    #     get_detail(code_list)
        
    # elif 'fundsearch' in website:
    #     code_list=get_search_code(start_page)
    #     get_detail(code_list)
    
    # elif 'manager' in start_page:
    #     code_list=get_manager_code(start_page)
    #     get_detail(code_list)
    code_list=['000968','510880','160716','001594','206018','161716','110007','110017','002459','320021','001001','162412',
    '050111','510510','002738','420102','485011','161115']
    print('共计检查基金数目：',len(code_list))
    get_detail(code_list)
    
    driver.quit()
    
    
    

