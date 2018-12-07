#import  os
# a=os.popen('ping 8.8.8.8')    #popen执行命令
# print(a.read())

#获取当前所在的位置
#print(os.getcwd())

#切换目录
#os.chdir(r'C:\Users\zhang\Desktop')

#创建目录
#os.mkdir('aaaa') #如果不加路径就在当前目录下创建
#创建递归目录
#os.makedirs(r'C:\Users\zhang\Desktop\qwe')
#删除递归空目录
#os.removedirs()
#删除文件
#os.remove('a.txe')
#删除空目录
#os.rmdir(r'C:\Users\zhang\Desktop\qwe')
#获取当前目录下的所有文件
#print(os.listdir(r'C:\Users\zhang\Desktop'))
#重命名
#os.rename('旧文件名','新文件名')
#os.rename('qwe.py','ewq.py')
#将文件名与路径分隔开
#主意：分割的是字符串，与有无此文件和路径无关
#print(os.path.split(r'C:\Users\zhang\Desktop\aaa.py'))
#将文件的后缀名与路径分割开
#print(os.path.splitext(r'C:\Users\zhang\Desktop\aaa.py'))
#判断是否为普通文件
#print(os.path.isfile('ewq.py'))
#判断是否为目录文件
#print(os.path.isdir('qwe.py'))
#判断是否为链接文件
#print(os.path.islink('1'))
#for i in os.listdir():
 #   if os.path.splitext(i)[1]=='py':
 #      print(i)
# a=0
# b=0
# os.chdir(r'C:\Users')
# for i in os.listdir(r'C:'):
#     if os.path.isdir(i):
#         a+=1
#     else:
#         b+=1
#     print(a)
#xlwt 作用  #gei excel表格写入数据
#xlrd            #读取excel表格中的数据
#xlutils     #给excel表格中追加数据
#打开一个文件
#import xlwt
#f=xlwt.Workbook(encoding='utf-8')
#添加一个标签页,括号中也标签页的名称.
#sheet=f.add_sheet('python操作excel表')


#sheet.write(0,0,'姓名')
#sheet.write(0,1,'班级')
#sheet.write(0,2,'年龄')
#for i in range(1,31):
   # sheet.write(i,0,'小')
  #  sheet.write(i,1,'12岁')
 #   sheet.write(i,2,'10班')#第一行数字代表多少行，第二个数字代表多少列，第三个字符串代表写入的内容
#保存文件
#f.save('qwqe.xls')
#import pymysql
#import xlwt
#a=pymysql.connect(host="192.168.0.191",port=3306,user='root',passwd='123456')
#aaa=a.cursor()
#aaa.execute('use test;')
#aaa.execute('create table biao6(姓名 char(222),年纪 int, 班级 char(23));')
#list=['小猪',1,'佩奇']
#for i in range(30):
 #   aaa.execute('insert into biao6  values("{}","{}","{}") '.format(list[0],list[1]+i,list[2]))
  #  a.commit()

#aaa.execute('select * from biao6;')
# shuju = aaa.fetchall()
# aaa.execute('desc biao6;')
# b=aaa.fetchall()
# print(b)
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('python操作excel表')
#sheet.write(0,0,b[0][0])
#sheet.write(0,1,b[1][0])
#sheet.write(0,2,b[2][0])
#for d in range(len(shuju )):
 #    sheet.write(d+1,0,shuju[d][0])
#     sheet.write(d+1,1,shuju[d][1])
#     sheet.write(d+1,2,shuju[d][2])
#f.save('www1.xls')
#吧数据库中的调到excel中
#
# with open('a.txt','w',encoding='utf-8')as q:
#    aaa.execute('select * from biao6;')
#    i=aaa.fetchall()
#    aaa.execute('desc biao6;')
#    b=aaa.fetchall()
#    print(b)
#    q.write('{},{},{}'.format(b[0][0],b[1][0],b[2][0]))
#     q.write('\n')
#     for d in range(2,32):
#        q.write('{},{},{}'.format(i[1][0],i[1][1],i[1][2]))
#        q.write('\n')
#        q.close
#吧数据库掉到文件中

# with open('a.txt','r',encoding='utf-8')as q:
#    c=q.readline()
#    c=c.split('\n')[0]
#    c=c.split(',')
#    d=q.read()
#    d=d.split('\n')[0]
#    d=d.split(',')
#    print(d)
# import pymysql
# a=pymysql.connect(host="192.168.0.191",port=3306,user='root',passwd='123456')
# aaa=a.cursor()
# aaa.execute('use test;')
# aaa.execute('create table fxsb({} char(222),{} int,{} char(222));'.format(c[0],c[1],c[2]))
# for i in range(1,31):
#    aaa.execute('insert into fxsb  values("{}","{}","{}") '.format(d[0],d[1],d[2]))
#    a.commit()
# aaa.execute('select * from fxsb;')
# print(aaa.fetchall())
#吧文件中掉到数据库中

#读取excel表格
#import xlrd
#f=xlrd.open_workbook('qwqe.xls')
#两种获取标签页的方式    1：通过索引来获取
#sheet = f.nsheets
#print(sheet)#获取多少个标签页

#print(f.sheet_names()) #获取所有标签页的名字
#sheet=f.sheet_by_name('Sheet1')  #括号中填写操作的标签页名称
#sheet = f.sheets()[0]  #通过索引值来使用哪一个标签页
#a=sheet.nrows #获取文件中有多少行
#for i in range(a):
 #  print(sheet.row_values(i))
#print(sheet.row_values(0))  #读取第一行的内容

#print(sheet.ncols)  #获取多少列
#print(sheet.col_values(2)) #读取第几列的内容
#print(sheet.cell(0,0).value)  #读取某个单元格


#excel表格追加
# import xlrd
# from xlutils.copy import copy
# f=xlrd.open_workbook('qwqe.xls')  #打开文件
# new_f=copy(f)  #复制文件
# sheet = new_f.get_sheet(0)   #通过索引获取
# sheet.write(5,5,'哈哈哈')  #写入
# new_f.save('qwqe.xls')
#
# import xlrd
# f=xlrd.open_workbook('www1.xls')
# sheet=f.nsheets
# sheet=f.sheet_by_name('python操作excel表')
# c=sheet.row_values(0)
# w=[]
# print(c[0])
# for i in range(1,31):
#     d=sheet.row_values(i)
#     w.append(d)
# print(sheet.ncols)
# with open('c.txt','w+',encoding='utf-8')as q:
#     q.write(c[0]+',')
#     q.write(c[2]+'\n')
#     for j in w:
#         q.write('{},{},{}'.format(j[0],j[1],j[2]))
#         q.write('\n')
#     q.close()
#吧excel表中的数据掉到文件中

# import xlwt
# with open('b.txt','r',encoding='utf-8')as q:
#      a=q.readline()
#      a=a.split(',')
#      b=q.read()
#      b=b.split('\n')
#      print(b)
# f = xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('python操作excel表')
# sheet.write(0,0,a[0])
# sheet.write(0,1,a[1])
# sheet.write(0,2,a[2])
# for i in range(1,len(b)+1):
#     c = b[i-1].split(',')
#     sheet.write(i,0,c[0])
#     sheet.write(i,1,c[1])
#     sheet.write(i,2,c[2])
# f.save('qqq.xls')
#吧文件导入excel中

# import xlrd
# import pymysql
# f=xlrd.open_workbook('www1.xls')
# sheet=f.nsheets
# sheet=f.sheet_by_name('python操作excel表')
# c=sheet.row_values(0)
# print(c)
# w=[]
# for i in range(1,31):
#      d=sheet.row_values(i)
#      w.append(d)
# #print(w)
# a=pymysql.connect(host="192.168.0.26",port=3306,user='root',passwd='123456')
# aaa=a.cursor()
# aaa.execute('use test;')
# #aaa.execute('create table biao10 ({} char(222),{} int,{} char(222));'.format(c[0],c[1],c[2]))
# for j in w:
#     aaa.execute('insert into biao10 values("{}","{}","{}");'.format(j[0],j[1],j[2]))
#     a.commit()
# aaa.execute('select * from biao10;')
# b=aaa.fetchall()
# print(b)
#吧excel表格导入数据库中

#import paramiko
#封装了SSH协议，用于远程连接
#ssh123=paramiko.SSHClient()
#吧将要连接的主机添加到 know_hosts  文件中
#ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
#ssh123.connect(hostname='192.168.0.26',
 #                port=22,
  #              username='root',
   #             password='zhangjy')

#stuin,stuout,stuerr=ssh123.exec_command('ls -al')
#第一个变量：执行的命令，输入,输入的命令只能是有结果的命令
#第二个变量：命令的结果，输出
#第三个变量，命令的报错
#stuin,stuout,stuerr=ssh123.exec_command('ls -al /home')
#print(stuout.read().decode())
#ssh123.close()

#创建一个传输通道
#import paramiko
#ssh123=paramiko.Transport(('192.168.0.26',22)) #这个函数只能接受元祖
#ssh123.connect(username='root',password='zhangjy')
#传输文件使用sftp协议  创建一个sftp的实例
#sftp=paramiko.SFTPClient.from_transport(ssh123)
#从linux中下载文件到本地
#sftp.get('文件名，路径')
#例如sftp.get('/home/2.5050','./aaa.cfg')
#put是从本地上向linux上传文件
#sftp.put('文件名,路径')
#sftp.put('a.txt','/home/shells/b.ccc')
#sftp.close()

#发送邮件
# import smtplib  #发送邮件的协议
# import email.mime.text #处理发送的消息
# import email.mime.multipart  #处理邮件的表头
# sender='zhang15660600605@163.com'   #发送者
# recver='xcz20180718@163.com' #接收者，可多发
# server='smtp.163.com'
# passwd='hhxxttxs520'     #授权码
# #创建一个空邮件
# a=email.mime.multipart.MIMEMultipart()
# #发件人
# a['from']=sender
# #收件人
# a['to']=recver
# #主题
# a['subject']='小猪佩奇'
# #正文
# text="""
# 听说你喜欢facebook，买下来送你了!!!
# """
# #处理文本信息
# text=email.mime.text.MIMEText(text)
# #将处理后的信息添加到邮件里
# a.attach(text)

#添加附件；处理附件：以二进制的方式读取附件
# a1=email.mime.text.MIMEText(open('a.txt','rb').read(),'base64','utf-8')
# a1["Content-Type"]='application/octet-stream'
# a1["Content-Disposition"]='attachment;filename="a.txt"'
# a.attach(a1)
# a2=email.mime.text.MIMEText(open('b.txt','rb').read(),'base64','utf-8')
# a2["Content-Type"]='application/octet-stream'
# a2["Content-Disposition"]='attachment;filename="b.txt"'
# a.attach(a2)
# #
#定义服务器和端口
# smtp123=smtplib.SMTP_SSL(server,465)
# #登陆服务器
# smtp123.login(sender,passwd)
# #发送邮件
# smtp123.sendmail(sender,recver,a.as_string())
# #断开连接
# smtp123.close()

#时间模块
# import time
#时间戳  代表从公元1970年到现在经历的秒数
#print(time.time())
#本地时间 默认显示当前时间
#括号里的参数:时间戳  #括号外可以取下标值
# print(time.localtime())
#格式化成现代化时间
# print(time.strftime('%Y.%m.%d %w %H-%M-%S',time.localtime()))
#现代化时间格式成元祖
#print(time.strptime('1233 12 12','%Y %m %d'))

#a=time.strptime('2011 12 12','%Y %m %d')
#将元祖的时间转化为时间戳
#print(time.mktime(a))

#休眠
#time.sleep(2)
#print(123)
#输入一个现代化日期(年月日),输出今年是否为瑞年,输出今天是星期几，输出今年是一年中的第几天
# a=input('>>>')
# a=a.split(' ')
# c=(time.strptime('{} {} {}'.format(a[0],a[1],a[2]),'%Y %m %d'))
# print(c)
# if int(a[0])%4==0 and int(a[0])%100 != 0:
#     print('瑞年')
# elif int(a[0])%400==0:
#     print('瑞年')
# else:
#     print('不是瑞年')
# print('今天是周{}'.format(c[-3]+1))
# print('今天是一年的第{}天'.format(c[-2]))

# a=input('>>>')
# a=a.split(' ')
# c=(time.strptime('{} {} {}'.format(a[0],a[1],a[2]),'%Y %m %d'))
# print(c)
# d=time.mktime(c)-86400.0
# print(time.strftime('%Y %m %d', time.localtime(d)))


# class Excel:
#     def __init__(self,p):
#         self.page=p
#         return html
#     def sming(self):
#         patt=re.compile(r'title="(.*?)"',re.S)
#         items_1=patt.findall(self.qingqiu())
#         for i in items_1:
#             if '可试读' in i:
#                 continue
#             else:
#                 self.shuming.append(i)
#         return self.shuming
#     def zjia(self):
#         txt=xlrd.open_workbook('shu.xls')
#         new_txt=copy(txt)


#输入某年某月某日，判断这一天是这一年的第几天？
# import time
# a=input('>>>').split(' ')
# c=time.strptime('{} {} {}'.format(a[0],a[1],a[2]),'%Y %m %d')
# if int(c[0])%4==0 and int(c[0])%100!=0:
#     print('shi瑞')
# elif int(c[0])%400==0:
#     print('rui')
# else:
#     print('不是')
# print('今天是第{}天'.format(c[-2]))
#

#题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# a=int(input('>>>'))
# b=int(input('>>'))
# c=int(input('>'))
# d=[]
# d.append(a)
# d.append(b)
# d.append(c)
# d.sort()
# print(d)

#题目：暂停5秒输出。
# import time
# a=1
# b=2
# print(a)
# time.sleep(5)
# print(b)

#题目:有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
# a=1
# # b=1
# # for i in range(1,22):
# #     print ('{} {}'.format(a,b))
# #     if (i % 3) == 0:
# #         print ('')
# #     a=a+b
# #     b=a+b



#题目：判断101-200之间有多少个素数，并输出所有素数。
# h = 0
# for i in range(101,201):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)
#         h=h+1
# print(h)

#将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
# a=int(input(">>>"))
# for b in range(2,a):
#     for c in range(2,a):
#         for d in range(2,a):
#             for e in range(2,a):
#                 if b*c*d*e==a:
#                     print('{}*{}*{}*{}'.format(b,c,d,e))
# b=0                                                       #去掉文件中#和空行
# with open('q.txt','r',encoding='utf-8')as f:
#     a=f.readlines()
#     for i in (a):
#         if i=='/n' or  i.startswith('#')==True:
#              continue
#         else:
#             b=b+1
#     print(b)

# import socket
# sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.connect(('192.168.0.89',233))
# aaa='qwer'
# sock.send(aaa.encode('utf-8'))
# msg=sock.recv(1024)
# print(msg.decode('utf-8'))


