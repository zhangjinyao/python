# Tn = 0
# Sn = []
# n =int(input('n='))
# a =int(input('a='))
# for count in range(n):
#     Tn = Tn + a
#     a = a * 10
#     Sn.append(Tn)
#     print(Tn)
# def aa(y):
#     print('123')
#     print(y)
# aa()

# import pymysql
# import xlwt
#
# abc=pymysql.connect(host='192.168.0.69',port=3306,user='root',password='123456',charset='utf8')
# a=abc.cursor()
# a.execute('use test1;')
#a.execute('create table biao1(姓名 char(222),班级 int,年龄 char(222));'
# j=['xiao',1,2]
# for k in range(30):
#     a.execute('insert into biao1  values("{}","{}","{}");'.format(j[0],j[1]+k,j[2]+k))
#     abc.commit()
# a.execute('select * from biao1;')
# shuju=a.fetchall()
# print(shuju)
# a.execute('desc biao1;')
# b=a.fetchall()
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('python操作excel表')
# sheet.write(0,0,b[0][0])
# sheet.write(0,1,b[1][0])
# sheet.write(0,2,b[2][0])
# for d in range(len(shuju)):
#     sheet.write(d+1,0,shuju[d][0])
#     sheet.write(d+1,1,shuju[d][1])
#     sheet.write(d+1,2,shuju[d][2])
# f.save('www1.xls')
# with open('a.txt','w',encoding='utf-8')as q:
#     q.write('{} {} {}'.format(b[0][0],b[1][0],b[2][0]))
#     q.write('\n')
#     for i in range(len(shuju)):
#         q.write('{} {} {}'.format(shuju[i][0],shuju[i][1],shuju[i][2]))
#         q.write('\n')
#     q.close()

#
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# a=(('192.168.0.89',233))
# s.bind(a)
# s.listen(3)
# while True:
#     a,b=s.accept()
#     msg=a.recv(1024)
#     print(msg.decode('utf-8'))
#     reg='eqwe'
#     a.send(reg.encode('utf-8'))

# import requests
# import re
# import os
# url='http://www.doutula.com/article/list/?page={}'.format(2)
# hea={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36'}
# res=requests.get(url=url,headers=hea)
# html=res.content.decode('UTF-8')
# patt=re.compile(r'<a href="http://www.doutula.com/article/detail/[0-9]{7}" class="list-group-item random_list">')
# items=patt.findall(html)
# patt1 = re.compile(r'<div class="random_title">(.*?)<div class="date">')
# items1 = patt1.findall(html)
# for q, w in enumerate(items):
#     w = w.replace('<a href="', '').replace('" class="list-group-item random_list">','')
#     url=w
#     #print(url)
#     hea = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36'
#     }
#     res = requests.get(url=url, headers=hea)
#     html = res.content.decode('UTF-8')
#     patt3=re.compile(r'alt="(.*?)" onerror="this.src=(.*?)">')
#     items3=patt3.findall(html)
#     os.mkdir('{}'.format(items1[q]))
#     for z,x in enumerate(items3):
#         url3=x[1].replace("'","")
#         #print(url3)
#         respons = requests.get(url3)
#         tu=respons.content
#         with open('{}\{}.jpg'.format(items1[q],z),'wb') as f:
#             f.write(tu)
#             f.close()

