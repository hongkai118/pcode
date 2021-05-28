#正则表达式笔记
#    ——正则是推荐r'aaafaf'格式，进行转义，而不推荐\斜杠转移。r''不要用在文件路径上。
#    ——()配合findall 是只显示()里面的内容，优先级最高
#    ——(?:re) 返回括号内re规则的内容,具有分组功能
#    ——re.findall(),返回符合条件的list
#    ——re.sub(pattern,替换内容 , string[, count]) count表示要替换的次数
#    ——\w 不等于还包括了中文，所以不等于[A-z0-9_-]
#    ——\s 各种制表符，空格等等

import re
#*************************具体实例如下*********************


#1. 匹配邮箱
# 分析，例如：kyle.you@isaac-kenneth.com
#    -最前面3个字母数字以上：[A-z0-9_-]{3,}
#    -最二部分.you, 0次或多次：(?:\.[A-z0-9]+)*
#    -第三部分：@
#    -第四部分issac-kenneth： [A-z0-9_-]+
#    -第五部分.com或.com.cn:   (?:\.[A-z0-9]{2,5}){1,2}

# strs = '我的私人邮箱是Az-huwjwh@outlook.com大幅度反对法的，adddd_123@163.com公司邮箱是123456@qq.org，kyle.you@isaac-kenneth.com.cn.cdcc麻烦333820202@qq.com登记一下？'
# pattern =re.compile(r"[A-z0-9-_]{3,}(?:\.[A-z0-9]+)*@[A-z0-9_-]+(?:\.[A-z0-9]{2,5}){1,2}")
# result = pattern.findall(strs)
# print(result)

#2. 身份证号码
# 511024 1988 01 18 022 X
# xxxxxx yyyy MM dd 375 0 十八位
# \d{6}  [19|20]

# 地区： [1-9]\d{5}
# 年的前两位： (18|19|([23]\d)) 1800-2399
# 年的后两位： \d{2}
# 月份： ((0[1-9])|(10|11|12))
# 天数： (([0-2][1-9])|10|20|30|31) 闰年不能禁止29+
# 三位顺序码： \d{3}
# 两位顺序码： \d{2}
# 校验码： [0-9Xx]

# strs = '小明的身份证号码是51102419880318022X对方对方的，5110242880180222Y,511024208812180222手机号是13987692110'

# #网上例子
# # pattern = re.compile(r"[1-9]\d{5}(?:18|19|(?:[23]\d))\d{2}(?:(?:0[1-9])|(?:10|11|12))(?:(?:[0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]")

# #我自己写的
# pattern = re.compile(r"\d{6}(?:19|20)\d{2}(?:(?:0[1-9])|(?:11|12|10))(?:[0-2][1-9]|30|31|20|10)\d{3}[0-9Xx]")
# result = pattern.findall(strs)
# print(result)

# #3. 手机号
# strs = '小明的身份证号码是51102419880318022X对方对方的，5110242880180222Y,511024208812180222手机号是14987692110'
# #1 3 987692110
# # 1
# # 3-9
# # 9位数字

# pattern=re.compile(r"")
# pattern = re.compile(r"1[3-9]\d{9}")
# result = pattern.findall(strs)
# print(result)


# 4. 网页
# strs = 'Python官网的网址是https://www.python.org/,http://zhuanlan.zhihu.com/p/338826624'

# #自己写的


# # 5. 其他自己测试
# strs='截至2020-06-30，东方新能源汽车混合 的基金机构持有0.07亿份，占总份额的2.41%，个人投资者持有2.94亿份，占总份额的100.00%'

# pattern = re.compile(r"\d{1,3}\.\d{2}%")
# result = pattern.findall(strs)
# print(result[-1])

# # 6. sub测试

# strs='我时一个22粉刷匠，33粉刷，55粉刷呀'

# pattern=re.compile(r'\d{2}')
# result=re.sub(pattern,'***',strs,2)
# print(result)

# 7. 只取其中某一部分内容
strs='我时一个2)2粉刷匠，33)粉刷，55)粉(刷)呀'
pattern=re.compile(r"\d{2}(\))")
result=pattern.findall(strs)
print(result)