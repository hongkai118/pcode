#ustr='http:\u002F\u002Fmov.bn.netease.com\u002Fopen-movie\u002Fnos\u002Fmp4\u002F2015\u002F03\u002F30\u002FSAL1FS8TF_sd.mp4'

#int('str',base=10)用法 base默认10进制，可支持2，8，10，16进制

#常见编码方法
s='你好'

#编码
print(s.encode('utf-8')) #UTF-8编码一个汉字占3个字节，英文1个字节
print(s.encode('gbk')) #GBK编码 一个汉字占2个字节，英文1个字节

#解码:bytes.decode(encode='编码类型')
y1=s.encode('utf-8')
y2=s.encode('gbk')
print(y1.decode(encoding='utf-8'))
print(y2.decode(encoding='gbk'))

#ord和crd用法
s='/'
my_num=bin(ord(s)) #bin(10进制数字)转为2进制字符串，ord('你') #返回'你'的unicode编码的10进制数字
print(chr(int(my_num,2))) #chr(0b00101111) #传入2进制数值，返回对应的unicode结果




