#这次的代码，不好用，因为“登录smtp服务器后最多只能发送5封邮件，就会超出限制报错”
#不能：登录一次，发送N次，关闭服务器;(N次太多报错)
#只能：登录一次，发送一次，关闭服务器，再重新登录，再发送一次，关闭服务器

import smtplib
from email.mime.multipart import MIMEMultipart #邮件
from email.mime.text import MIMEText #内容
from email.mime.image import MIMEImage #图片
from email.mime.application import MIMEApplication #附件


sender = 'kyle.you@isaac-kenneth.com'
to_list = ['kyle.you@isaac-kenneth.com','182395178@qq.com']
cc_list = ['182395178@qq.com','2304961591@qq.com']
subject = '连续发送两次，间隔2秒'

#写邮件
em = MIMEMultipart() #实例化一个邮件
em['Subject'] = subject
em['From'] = sender
#em['To'] = ",".join(to_list)
em["Cc"] =receiver

#邮件内容
file = open(r'd:/pp/code/lianxi/6Email/1.txt','r',encoding='utf-8')
jd=file.read()
file.close()

content = MIMEText(jd)

em.attach(content)

#发送邮件--用公司邮箱

#1. 先连接上smtp服务器
smtp = smtplib.SMTP()
smtp.connect('smtp.263.net')
#2.登录
auth_pwd='KyleKyleKyle0'
smtp.login(sender,auth_pwd)

#3. 发送邮件
smtp.send_message(em)

print('发送完成')

#4. 关闭连接
smtp.close()

'''
#发送邮件--采用QQ邮箱，#不知道为什么，在已发送邮件里面没有，但是在收件人的收件箱里面有
smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com')

auth_pwd = 'nexhtxzfusjtbijb'
smtp.login(sender,auth_pwd)

smtp.send_message(em)

print('发送完成')
'''


