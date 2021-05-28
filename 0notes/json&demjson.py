
demjson: 将不规则的json，封装为json数据
json：字典格式文件
    - 调整格式网站：https://www.sojson.com/

字符串变为字典方法：
    ——方法1： dict = demjson.decode('字符串')
    ——方法2： dict = json.loads('字符串')

字典变为字符串：
    ——方法1： strs = json.dumps(dict)


#实例代码1：将字符串变为字典

import demjson
import requests

r = requests.get(url)
r.encoding ='utf-8'
html=r.text[14:-1] #将html文件（str类型）多余的字符去掉，只留下大括号{key:vaule}的内容，大括号之外的所有内容都要去掉。
jj_lists=demjson.decode(html) #把内容转成json格式后，直接就成为“字典”了，可以直接用字典方式调用。
max_num = len(jj_lists['datas']) 
print('总共获取{}支基金'.format(max_num))


