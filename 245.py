#爬虫

#模仿浏览器，根据自己制定的规则批量下载网络中的资源
#正则表达式：匹配文件中的内容
#模仿浏览器的模块：urllib , urllib3 , requests
#匹配内容的模块:re , bs4 ,xpath
#爬虫分类：1.聚焦爬虫（只爬取某个网站的资源）
           # 2.搜索爬虫(爬取整个网络的资源)
# #面向对象代码  爬虫第一步：分析网址的变化,并请求
#                    # 第二步：分析html文件（正则表达式），过滤并下载想要的资源
#                    #第三部：保存的权限和格式
#https://'www.qiushibaike.com/text/page/{}/'.format(2)
# import requests
# import re
# class a(object):
#     def qingqiu(self,page):
#             url='https://www.qiushibaike.com/text/page/{}/'.format(page)
#         # 发送请求
#             response=requests.get(url=url)
#         #读取结果的方式 1:以字符串的方式读取
#         #print(response.text)
#         #以字节流的方式读取
#         #print(response.content.decode('utf-8'))
#             html=response.content.decode('utf-8')
#             return html
#     def guolv(self,abc):
#         shuju=[]
#         patt =re.compile('<div class="content">(.*?)</div>',re.S)
#         items=patt.findall(abc)
#         for i in items:
#             i=i.replace('<span>','').replace('</span>','')
#             i=i.replace('<br/>','')
#             i=i.replace('<span class="contentForAll">查看全文','')
#             i=i.strip(i)
#             shuju.append(i)
#         return shuju
#     def save(self,shuju):
#         with open('b.txt','a',encoding='utf-8')as f:
#             for i in shuju:
#                 f.write(i+'\n')
# b=a()
# jieguo=b.qingqiu(2)
# shuju=b.guolv(jieguo)
# b.save(shuju)



# 导入正则模块  #只能匹配字符串
# 贪婪模式:尽可能多的去匹配最后的内容
# 非贪婪模式：尽可能少的去匹配最后的字符串
# 带有？的是非贪婪，带*的是贪婪
# .匹配任意一个字符，除了换行符
# import re
# a= """qwe123qwe3qweqwe"""
# #将要匹配的正则编译
# b=re.compile('QWE(.*)QWE'.I)  #re,S让.可以匹配包括换行符在内的所有字符  # .I 不区分大小写
# #到目的字符串中去查找
# c=b.findall(a)
# print(c)

#import requests
#import re
# url1='http://www.doutula.com/article/list/?page=1'
# head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36'}
# response=requests.get(url=url1,headers=head)
# html=response.content.decode('UTF-8')
# #print(html)
# patt=re.compile(r'http://www.doutula.com/article/detail/[0-9]{7}')
# items=patt.findall(html)
# for i in items:
#     response=requests.get(url=i,headers=head)
#     html1 = response.content.decode('UTF-8')
#     patt1=re.compile(r'<img src="https://ws(.*?)alt')
#     items1=patt1.findall(html1)
#     for j,i in enumerate(items1):
#         i=i.replace('"','')
#         i='http://ws'+i
#         a=requests.get(i)
#         res1=a.content
#         with open(r'C:\Users\zjy\Desktop\{}.jpg'.format(j),'wb')as f:
#             f.write(res1)
#             f.close()

# import requests
# import re
# url='https://book.douban.com/latest?icn=index-latestbook-all'
# heard={'User-Agent':'Mozil,.la/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
# res=requests.get(url=url,headers=heard)
# html=res.content.decode('utf-8')
# patt = re.compile(r'><img src="(.*?)"/></a>',re.S)
# patt1=re.compile(r'a href="https://book.douban.com/subject/[0-9]{8}/">(.*?)</a>',re.S)
# items=patt.findall(html)
# items1=patt1.findall(html)
# for j,i in enumerate(items):
#         mew_url=i
#         respons=requests.get(url=mew_url,headers=heard)
#         tu=respons.content
#         print(tu)
#         with open(r'C:\Users\zjy\Desktop\{}.jpg'.format(items1[j]),'wb') as f:
#                 f.write(tu)
#                 f.close()

# import requests
# import re
# a=1
# url='https://www.qiushibaike.com/8hr/page/{}/'.format(a)
# res=requests.get(url=url)
# html=res.content.decode('utf-8')
# patt=re.compile(r'<div class="content">(.*?)</div>',re.S)
# items=patt.findall(html)
# for i in items:
#         i=i.replace('<span>','').replace('</span>','').replace('<>','')
#         i=i.replace('<br/>','')
#         i.strip()
#         with open(r'C:\Users\zjy\Desktop\q.txt','a',encoding='utf-8') as f:
#                 f.write(i+'\n')
#                 f.close()

# import re
# import requests
# url='http://www.biquge.com.tw/0_748/526210.html'
# res=requests.get(url=url)
# html=res.content.decode('gbk')
# patt=re.compile(r'<div id="content">(.*?)</div>',re.S)
# items=patt.findall(html)
# for i in items:
#     i=i.replace('<br />','').replace('&nbsp;&nbsp;&nbsp;&nbsp;（每一个钟头上传一章，直到传完二十章！红票和珍藏别忘了～','')
#     i=i.replace('&nbsp;&nbsp;&nbsp;&nbsp;','')
#     i.strip()
#     with open(r'C:\Users\zjy\Desktop\.txt', 'a', encoding='gbk') as f:
#                  f.write(i+'\n')
#                  f.close()

#tcp
# import socket
# sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #连接服务器  接受的参数也是元祖
# sock.connect(('192.168.0.67',233))
# aaa='n hao'
# sock.send(aaa.encode('utf-8'))
# msg=sock.recv(1024)
# print(msg.decode('utf-8'))


#udp
# import socket
# #创建socket  封装协议
# soc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #发送数据请求
# a=('192.168.0.67',233)
# reg='买了否冷'
# soc.sendto(reg.encode('utf-8'),a)
# #接受响应
# c=soc.recv(1024)
# print(c.decode('utf-8'))

#
# class aaa():
#     def aa(self):
#         a=1
#         return a
# b=aaa()
#
# class bbb():
#     def aa(self):
#         a=2
#         return a
# c=bbb()
#
# class ccc(bbb,aaa):
#     pass
# print(ccc().aa())



# import socket
# a=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# a.connect(('192.168.0.23',333))
# aaa='qweqwewqe'
# a.send(aaa.encode('utf-8'))
# reg=a.recv(1024)
# print(reg.decode('utf-8'))



