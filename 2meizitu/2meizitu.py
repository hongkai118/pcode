import requests
import os 
import time
from bs4 import BeautifulSoup
save_path = "e:\\spider_file"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'referer': 'https://www.mzitu.com/'} #mzitu网站,referer很重要，不然不能访问网页

def access_page(url):
    try:
        r=requests.get(url,headers =headers,timeout = 30)
        r.raise_for_status
        r.encoding = 'utf-8'
        return r.text
    except:
        return "访问网页不成功"

#获取所有，套图的，链接和名字，并创建文件目录
def imgs_list_and_name(html):
    soup = BeautifulSoup(html,'html.parser')
    imgs_lists = soup.find('ul',id='pins').find_all('li')
    lists_names =[]
    for i in imgs_lists: ##############################
        imgs_link = i.find('a').get('href')
        imgs_name = i.find('span').string
        temp_lists = [imgs_link,imgs_name]
        lists_names.append(temp_lists)
        #print(lists_names)
        file_path = save_path+'\\'+imgs_name
        create_dir(file_path)        
    return lists_names

#下载一套图里面的所有图片并保存
def get_imgs(url, imgs_dir):
    print('-------------!!!!!!!!!!!!!!---',url)
    html = access_page(url)
    soup = BeautifulSoup(html,'html.parser')
    max_num = soup.find('div',class_='pagenavi').find_all('a')[4].string
    print("此套图片数量：",max_num)
    for i in range(int(max_num)):
        i = i+1
        img_page = url +'/' +str(i)
        html = access_page(img_page)
        soup = BeautifulSoup(html,'html.parser')
        img_src = soup.find('img',class_='blur').get('src')
        img_name = str(img_src).split('/')[-1]
        try:
            img_c=requests.get(img_src,headers =headers,timeout = 30)
            img_c.raise_for_status
        except:
            print("获取网页失败：{}".format(img_src))
            pass
            
        
        file_os_path = save_path+'\\' + imgs_dir +'\\'+img_name 
        if os.path.isfile(file_os_path):
            print('图片已存在：',file_os_path)
            pass
        else:
            with open(file_os_path,'wb') as f:
                f.write(img_c.content)
                print('图片已保存：',file_os_path)
                f.close()
                
        time.sleep(1)

def create_dir(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)

def main():
    url = 'https://www.mzitu.com/xinggan/'
    html=access_page(url) #访问网页
    imgs_lists = imgs_list_and_name(html) #成套的link和名字的列表，以及创建文件
    print('总共有多少套图片：',len(imgs_lists))
    for i in imgs_lists:
        imgs_link = i[0]
        imgs_name = i[1]
        get_imgs(imgs_link,imgs_name) #其中一套的图片下载

main()