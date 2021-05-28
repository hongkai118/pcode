selenium的基本使用

作用：
    ——获取网站动态加载的数据
    ——便捷的实现模拟登录
    
可以进行的操作
    —— 标签定位：search=driver.find_element_by_id('d')；如果属性值里面包括了空格<div class='aaa bbb'>，只需要取class的值'aaa'或者'bbb'就可以。
    —— 标签交互: search_input.send_keys('要输入的内容')
    —— 点击按钮：btn.click()
    —— 刷新页面：driver.refresh()
    —— 滑动鼠标：driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") #滑倒底部
        ——如果需要返回值的需要加return:driver.execute_script("return window.xxxxxxx")
    —— 执行js代码：driver.execute_script('js代码')
    —— 回退，前进：driver.back()，driver.forward()
    —— 关闭浏览器：driver.quit()

注意事项，无法获取数据时：
    —— selenium是读取网页当前的页面的信息，有很多页面是通过鼠标滑动后动态加载，
    需要滑动鼠标后有了相应的数据后才能取解析到，不然解析不到。办法：滑动鼠标后，再读取源文件
    —— 有些时候网速慢，页面没有加载出来，无法解析数据。办法：等待几秒钟，再获取源文件。 
    —— 如果定位的标签在Frame标签中，需要切换到当前frame: driver.switch_to.frame('标签的id值')

动作链：（具体内容查看python爬虫P52)
    —— 导入: from selenium.webdriver import ActionChains



实例代码目录：
    ——实例代码1：用正常情况下打开网页，并用xpath解析
    ——实例代码2：不打开网页，用xpath解析网页
    ——实例代码3：点击按钮
    ——实例代码4：获取cookie
    ——实例代码5：禁止chrome浏览器弹窗

反爬虫常见解决方式：
    ——网站监测出为webdriver==再浏览器console里面输入:window.navigator.webdriver 值为True表示webdriver,否则为undefind
        ——解决办法：opt.add_argument("--disable-blink-features=AutomationControlled") #88版本之后


****************实例代码1：用正常情况下打开网页，并用xpath解析*********************

from selenium import webdriver

#实例化一个浏览器对象
driver = webdriver.Chrome()

#对指定url发起请求
driver.get('https://cn.investing.com/rates-bonds/china-10-year-bond-yield')

#获取页面源码数据
html = driver.page_source

#用xpath解析页面源码
from lxml import etree
tree = etree.HTML(html)
num=tree.xpath('//*[@id="last_last"]/text()')[0]
print(num)

********************实例代码2：不打开网页，用xpath解析网页**********************
from selenium import webdriver

#实例化一个浏览器对象
opt = webdriver.ChromeOptions()
opt.add_argument('--disable-gpu') #禁止GPU渲染
opt.add_argument('--headless') #无界面模式
opt.add_argument("--disable-blink-features=AutomationControlled") #反爬手段：使浏览器无法检测为webdriver

#不加载图片加快访问速度
opt.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2}) 
#1.设置为开发者模式，防止被各大网站识别使用了selenium;2.禁止打印日志
opt.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=opt)

#对指定url发起请求
driver.get('https://cn.investing.com/rates-bonds/china-10-year-bond-yield')

#获取页面源码数据
html = driver.page_source

#用xpath解析页面源码
from lxml import etree
tree = etree.HTML(html)
num=tree.xpath('//*[@id="last_last"]/text()')[0]
print(num)
driver.quit() 


********************实例代码3：点击按钮**********************
from selenium import webdriver

#实例化一个浏览器对象
opt = webdriver.ChromeOptions()
opt.add_argument('--disable-gpu') #禁止GPU渲染
opt.add_argument('--headless') #无界面模式
#1.设置为开发者模式，防止被各大网站识别使用了selenium;2.禁止打印日志
opt.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=opt)


#对指定url发起请求
driver.get('url网址')
html1=driver.page_source #没有点击加载按钮时的页面源代码。

more_jj=driver.find_element_by_xpath('//*[@id="jj"]/p/a') #通过xpath定位按钮位置
more_jj.click() #点击按钮
time.sleep(3) #休息几秒，等待页面加载数据
html2 = driver.page_source #获得加载后的页面源代码

***********实例代码4：获取cooike，读取cookie*****

#登录后
driver.get('www.xxxx.com')
#获取cooike
dictCookies =driver.get_cookies()
jsonCookies = json.dumps(dictCookies)

with open('weibo_cookies.json','w') as f:
    f.write(jsonCookies)
print('Cooikes下载到weibo_cookies.json')

#访问cooike
#1. 打开网页-->删除之前的cooike-->加载cooike-->重新访问需要访问的页面（此时已经登录）
driver.get('https://weibo.com/')
driver.delete_all_cookies()

#加载cookies一下内容格式都是固定的，只需要修改domain的值
with open('weibo_cookies.json', 'r', encoding='utf-8') as f:
    listCookies = json.loads(f.read())
for cookie in listCookies:
    driver.add_cookie({
        'domain': '.weibo.com',
        'name': cookie['name'],
        'value': cookie['value'],
        'path': '/',
        'expires': None
    })

#访问登陆后页面
driver.get('https://weibo.com/1808276353/fans?rightmod=1&wvr=6')


***********实例代码5：进制chrome浏览器的通知弹窗****************

from selenium import webdriver
import time
 
options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values' :
        {
        'notifications' : 2
         }
}
options.add_experimental_option('prefs',prefs)
driver = webdriver.Chrome(chrome_options = options)
 
driver =webdriver.Chrome()
driver.get("https://weibo.com/")
driver.implicitly_wait(10)
time.sleep(2)