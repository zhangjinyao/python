import pymysql
import os
abc=pymysql.connect(host='192.168.0.123',port=3306,user='root',password='123456',charset='utf8')
a=abc.cursor()
# f=open('文本','r+',encoding='utf-8')
# f.write('姓名 年龄 班级 性别\n')
# for i in range(1,11):
#     f.write('小明 21 二班 男\n')
# b=f.readlines()
# print(b)
# f.close()
# a.execute('use text;')
#
# for j in b:
#     j=j.replace('\n','')
#     c = j.split(' ')
#     if c[0]=='姓名':
#         a.execute('create table biao10({} char(30),{} char(30),{} char(30),{} char(30));'.format(c[0],c[1],c[2],c[3]))
#     else:
#         a.execute('insert into biao10 values("{}","{}","{}","{}");'.format(c[0],c[1],c[2],c[3]))
# a.execute('select * from biao10;')
# o=a.fetchall()
# print(o)





# a.execute('use text;')
# a.execute('select * from yy11;')
# b=a.fetchall()
# print(b)
# a.execute('desc yy11;')
# d=a.fetchall()
# with open('n.txt','w+',encoding='utf-8') as f:
#     f.write("{},{},{}".format(d[0][0],d[1][0],d[2][0])+'\n')
#     for i in b:
#         f.write("{},{},{}".format(i[0],i[1],i[2])+'\n')
# import xlwt
# with open('n.txt','r+',encoding='utf-8') as f:
#     a=f.readlines()
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('sheet1')
# for j,i in enumerate(a):
#     i=i.replace('\n','')
#     # print(i)
#     i=i.split(' ')
#     # print(i)
#     for m in i:
#         m=m.split(',')
#         print(m)
#         sheet.write(j,0,m[0])
#         sheet.write(j, 1, m[1])
#         sheet.write(j, 2, m[2])
# f.save('a.xls')




    














