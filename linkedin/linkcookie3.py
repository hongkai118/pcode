from selenium import webdriver
from lxml import etree
import json
import time
import sys
import msvcrt

opt = webdriver.ChromeOptions()
opt.add_argument('--disable-gpu')  # 禁止GPU渲染
opt.add_argument('--headless') #无界面模式
# 1.设置为开发者模式，防止被各大网站识别使用了selenium;2.禁止打印日志
opt.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=opt)
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

def get_linkedin_cookies():
    driver.get('https://www.linkedin.com/uas/login')
    driver.implicitly_wait(3)

    #输入账号和密码
    # user = '182395178@qq.com'
    # pwd = 'DD127127'
    user=input('Linkedin账户：')
    pwd =pwd_input('Linkedin密码：')
    print('')
    user_name=driver.find_element_by_id('username')
    pass_word=driver.find_element_by_id('password')
    user_name.send_keys(user)
    pass_word.send_keys(pwd)

    #点击确定
    btn=driver.find_element_by_xpath('/html/body/div/main/div[2]/div[1]/form/div[3]/button')
    btn.click()
    driver.implicitly_wait(3)
    time.sleep(3)

    print('耐心等待几十秒')

# '''
#     #输入验证码
#     my_name = False #用来判断验证码

#     #1. 如果找到'pin'标签，则判断为要输入验证码，输入后获得获得cookie
#     try: 
#         auth_row=driver.find_element_by_name('pin') 
#     except:
#         auth_row=False 

#     #如果auth_row有值，则说明有验证码，输入验证码
#     if auth_row != False: 
        
#         click_counts= 1 #用来计数，输入了几次验证码

#         while my_name==False:

#             while True:
#                 auth_pwd=input('验证码(6位数字):')
#                 if len(str(auth_pwd)) != 6:
#                     print('验证码输入不合法，请重新输入....')
#                 else:
#                     break

#             if click_counts>=2: #如果第二次验证码，就重新定位下
#                 driver.refresh()
#                 time.sleep(3)
#                 auth_row=driver.find_element_by_name('pin')
            
#             auth_row.send_keys(auth_pwd)
#             click_counts=click_counts+1 #点击一次后计数器加一
#             #点击确定
#             pin_btn=driver.find_element_by_xpath('//*[@id="email-pin-submit-button"]')
#             pin_btn.click()
#             driver.implicitly_wait(3)
#             time.sleep(3)

#             html = driver.page_source
#             tree=etree.HTML(html)

#             try:
#                 #通过判断是否有名字来，判断是否登录成功;就算用的是全路径，Linkeidn还是经常在变换。
#                 my_name = tree.xpath('/html/body//div[1]/div[2]/a/div[2]/text()')[0]
#                 print('Dear {},登录成功，欢迎使用Linkedin...'.format(my_name.strip()))
#                 break
#             except:
#                 my_name = False
#                 print('验证码错误，请重新输入....')

    #1. 如果找到'pin'标签，则判断为要输入验证码，输入后获得获得cookie
    try: 
        auth_row=driver.find_element_by_name('pin') 
    except:
        auth_row=False 
    
    if auth_row:
        auth_pwd=input('验证码(6位数字):')
        auth_row.send_keys(auth_pwd)

        #点击确定
        pin_btn=driver.find_element_by_xpath('//*[@id="email-pin-submit-button"]')
        pin_btn.click()
        driver.implicitly_wait(3)
        time.sleep(2)
        driver.get('https://www.linkedin.com/uas/login')
        driver.implicitly_wait(3)
        time.sleep(2)

        html = driver.page_source
        tree=etree.HTML(html)

        try:
            #通过判断是否有名字来，判断是否登录成功;就算用的是全路径，Linkeidn还是经常在变换。
            my_name = tree.xpath('/html/body//div[1]/div[2]/a/div[2]/text() | /html/body/div[7]/div[3]/div/div/div/div/div/div/div[1]/div[1]/a/div[2]/text()')[0]
            print('Dear {},登录成功，欢迎使用Linkedin...'.format(my_name.strip()))
        except:
            print('没有检测到名字，不过有可能已经登录成功,先去试试能不能下载信息了')        


    #如果auth_row=False说明没有验证码，则直接判断是否登录成功。
    else: 
        html=driver.page_source
        tree=etree.HTML(html)
        try:
            my_name = tree.xpath('/html/body//div[1]/div[2]/a/div[2]/text() | /html/body/div[7]/div[3]/div/div/div/div/div/div/div[1]/div[1]/a/div[2]/text()')[0]
            print('Dear {}, 欢迎使用Linkedin...'.format(my_name.strip()))
        except:
            print('账号密码有误，请重新运行.')
            sys.exit(0)

    #获得cookies并转化成Json格式（json格式就是字典格式）
    dictCookies=driver.get_cookies()
    jsonCookies=json.dumps(dictCookies)

    #将cookie存储为json文件。
    with open('link_cookies.json','w') as f:
        f.write(jsonCookies)

    print('已将Linkedin的Cookies存储到文件："link_cookies.json"')


if __name__=='__main__':
    print('link_login版本：3.3')
    print('发布时间：2021-4-23')
    get_linkedin_cookies()
    driver.quit()