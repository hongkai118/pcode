import os
import time
import requests
from bs4 import BeautifulSoup

sava_path = "e:\\meizi"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Referer': 'https://www.mzitu.com/'
}

def access_page(url):
    try:
        r=requests.get(url,headers = headers, timeout = 30)
        r.raise_for_status
        r.encoding = 'utf-8'
        return r.text
    except:
        print('错误代码：',r.status_code)
        return "登录网页失败"

def get_all_lists(html):
    soup = BeautifulSoup(html,'html.parser')
    temp = soup.find('ul',id='pins').find_all('li')
    print(len(temp)) #24
    names_lists =[]
    for i in temp:
        imgs_link = i.find('a').get('href')
        imgs_name = i.find('span').string
        print(imgs_link,imgs_name)
        a_list = [imgs_link,imgs_name]
        names_lists.append(a_list)

    #获取主页的所有没一套图片的链接和名字，并返回一个列表   
    return names_lists

def download_imgs(imgs_link,imgs_dir):
    #获取imgs_link, 创建目录，下载一整套图片
    r= requests.get(imgs_link,headers =headers,timeout = 30)
    soup = BeautifulSoup(r.text,'html.parser')
    max_num = soup.find('div',class_='pagenavi').find_all('a')[4].find('span').string
    print("此套图片有:{}张".format(max_num))
    for i in range(int(max_num)):
        i = i + 1
        url = imgs_link +'/' +str(i)
        html =access_page(url)
        soup_1 = BeautifulSoup(html,'html.parser')
        pic_src = soup_1.find('img',class_='blur').get('src')
        pic_name = str(pic_src).split('/')[-1]

        #下载图片
        img_c = requests.get(pic_src,headers=headers,timeout=30)

        #保存图片
        imgs_path = imgs_dir+'\\'+pic_name
        if os.path.isfile(imgs_path):
            print("图片已存在:",imgs_path)
        else:
            with open(imgs_path,'wb') as f:
                f.write(img_c.content)
                print('图片已保存：',imgs_path)
                f.close()
        time.sleep(0.2)


def create_dir(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)

def main():
    links_names = []
    url = 'https://www.mzitu.com/xinggan/'
    html = access_page(url) #访问网页
    links_names = get_all_lists(html) #获取Lists(links，names)
    for i in links_names[:10]:
        imgs_link = i[0]
        imgs_name = i[1]
        #创建文件目录,
        imgs_dir = sava_path+'\\'+imgs_name #用套图名字来命名文建目录
        create_dir(imgs_dir)  #创建文件目录
        download_imgs(imgs_link,imgs_dir) #通过”链接“，下载图片到指定”目录“

main()
    

