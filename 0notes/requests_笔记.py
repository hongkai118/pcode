import requests
import json

#代码框架
try:
    r=requests.get(url,timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding #或者r.encoding = 'utf-8'
    return r.text
except:
    return "获取网页失败"



#1>>Get
# 给url传递参数
url = 'https://www.baidu.com/s'
param = {'key1':'value1','key2':'velue2'}
r = requests.get(url,params=param)
print(r.url) #打印结果：https://www.baidu.com/s?key1=value1&key2=velue2

#给url传递参数，参数所维列表
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url) #http://httpbin.org/get?key1=value1&key2=value2&key2=value3

#2 二进制相应内容
r = requests.get('https://www.baidu.com')
print(r.content[:100]) #二进制响应内容
print(r.text[:100])    #正常文本

#3 响应Json内容
r = requests.get('https://api.github.com/events')
r.json()

#2>> Post 请求
#1）只需简单地传递一个字典给 data 参数,你的数据字典在发出请求时会自动编码为表单形式
payload = {'key1':'value1','key2':'value2'}
r = requests.post('http://httpbin.org/post',data=payload)
print('\n------------------------------------------\n')
print(r.text)
#打印结果如下

  "form": {
    "key2": "value2",
    "key1": "value1"
  },

#2）你还可以为 data 参数传入一个元组列表。在表单中多个元素使用同一 key 的时候，这种方式尤其有效
payload = (('key1', 'value1'), ('key1', 'value2'))
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)
#打印结果如下

{
  
  "form": {
    "key1": [
      "value1",
      "value2"
    ]
  },
  
}

#3>> Post实例，处理百度翻译