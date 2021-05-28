代理相关网站：
    - 快代理
    - 西祠代理
    - www.goubanjia.com
    - www.xicidaili.com
    - www.66ip.cn
    - www.youdaili.net
    - www.kuaidaili.com/free/
    - http://www.ip3366.net
    - http://www.89ip.cn/
    - http://www.cz88.net/proxy/
    - goubanjia.com/
    - httpdaili.com/
    - http://proxy.mimvp.com/
    - dl.dainar.net/
    - http://superfastip.com/
    - http://ip.zdaye.com/dayProxy.html
    - data5u.com/
    - http://ip.kxdaili.com/
    - https://ip.ihuan.me/
    - http://www.iphai.com/

#----------------------------------------------------------------------------------------
#实例代码1 Selenium 添加代理
#添加代理
PROXY = "113.238.142.208:3128"
opt = webdriver.ChromeOptions()
opt.add_argument('--proxy-server={0}'.format(PROXY))
#opt.add_argument('--disable-gpu')  # 禁止GPU渲染
#opt.add_argument('--headless')  # 无界面模式
# 1.设置为开发者模式，防止被各大网站识别使用了selenium;2.禁止打印日志
opt.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=opt)
driver.get('https://www.baidu.com')

#-------------------------------------------------------------------------------------
#实例代码2：用Requests,封装代理IP
proxies = {'https':'113.238.142.208:3128'}
r=requests.get('https://cn.bing.com/',headers=headers,proxies=proxies,timeout=5)