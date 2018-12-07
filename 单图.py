#！ /usr/bin/env python
# -*- coding:utf-8 -*-
# import requests
# import re
# url='https://book.douban.com/latest?icn=index-latestbook-all'
# heard={'User-Agent':'Mozil,.la/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
# res=requests.get(url=url,headers=heard)
# html=res.content.decode('utf-8')
# pattern=re.compile(r'><img src="(.*?)"/></a>',re.S)
# pattern1=re.compile(r'a href="https://book.douban.com/subject/[0-9]{8}/">(.*?)</a>',re.S)
# items=pattern.findall(html)
# items1=pattern1.findall(html)
# for j,i in enumerate(items):
#         mew_url=i
#         respons=requests.get(url=mew_url,headers=heard)
#         tu=respons.content
#         with open(r'C:\Users\zjy\Desktop\{}.jpg'.format(j),'wb')as f:
#                     f.write(tu)
#                     f.close()


#题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
# a=int(input('>>>'))
# if a>=90:
#     print('A')
# elif a>=60 and a<90:
#     print('B')
# else:
#     print('C')


#题目：输出指定格式的日期
# import time
# if __name__ == '__main__':
#     print(time.strftime('%d/%m/%Y',time.localtime()))


#server端
#tcp
# import socket
# #创建socket  封装协议(ipv4,tcp)
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #绑定ip和端口号   bind接受的参数是元祖
# a=('192.168.0.85',6666)
# # 监听  数字指的是最大等待数
# s.bind(a)
# s.listen(123)
# while True:
#     a,b=s.accept()  #第一个结果是a： 客户端的链接信息   b:客户端的ip地址
#     c=a.recv(1024)  #接受数据   1024:每一次接受的最大字节数
#     print(c.decode('utf-8'))
#     reg='welcome'
#     a.send(reg.encode('utf-8'))

#udp
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# a=('192.168.0.85',333)
# #监听  最大等待数字3
# while True:
#     a,b=s.recvfrom(1024)  #接受数据   a：客户端发送的请求数据   b:客户端的ip地址
#     print(a.decode('utf-8'))
#     print(b)
#     #发送数据
#     msg='welcome'
#     s.sendto(msg.encode('utf-8'),b)
