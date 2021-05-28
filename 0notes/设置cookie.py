
Request 设置cookie方法：
    - 方法1： 自动设置用session方法，代码如下
        #1. 实例化一个session；后续用session代替request发送请求，session中会将cooike自动保存。
        session= requests.Session()

        #2. 用session访问一般是登录页，会自动保存cooike; 一般登录页都是post请求，请求数据在放入data中。
            #如果不需要登录，但需要cookie的，就用get访问首页获取cookie即可。
        r1=session.post(url=url,headers=headers,data={'key1':'value1','key2':'data2'})
        #3. 再用session访问，登录后的相关网页，就是已登录的状态。
        r2=session.get(url=url, headers=headers)

    - 方法2：手动设置，在headers的cookie中，将已登录界面的cooike，放进去：代码如下：
        headers ={
            'user-agent':'xxxxxx',
            'cookies':'xxxxxx'}


selenium 设置cookie方法：
    - 第一步：selenium模拟登录后，将cookie保存为json文件（json文件就是字典文件）
    - 第二步：打开网页-->删除cookie-->添加cookie-->访问网页。

    - 实例代码如下：
#第一步：登录且获取cookie
def get_linkedin_cookies():
    driver.get('www.xxxx.com/login')
    driver.implicitly_wait(3)

    #输入账号和密码
    user = 'xxxxxxxxxxxxxx'
    pwd = 'xxxxxxxxxxxx'
    user_name=driver.find_element_by_id('username')
    pass_word=driver.find_element_by_id('password')
    user_name.send_keys(user)
    pass_word.send_keys(pwd)

    #点击确定
    btn=driver.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[3]/button')
    btn.click()
    driver.implicitly_wait(3)
     
    #获得cookies并转化成Json格式（json格式就是字典格式）
    dictCookies=driver.get_cookies()
    jsonCookies=json.dumps(dictCookies)

    #将cookie存储为json文件。
    with open('link_cookies.json','w') as f:
        f.write(jsonCookies)

#第二步：打开网页，载入cookie
def login():
    #首先访问网页，删除现有cookie
    driver.get('https://www.linkedin.com/feed/')
    driver.delete_all_cookies()
    with open('link_cookies.json', 'r', encoding='utf-8') as f:
        listCookies = json.loads(f.read())
    
    #以下key为统一格式，不需要更改
    for cookie in listCookies:
        driver.add_cookie({
            'domain': '.linkedin.com',
            'name': cookie['name'],
            'value': cookie['value'],
            'path': '/',
            'expires': None
        })