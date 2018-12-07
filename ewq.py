#!/usr/bin/python   #指的用什么解释器运行脚本以及解释器所在的位置
# _*_ coding: utf-8 _*_    #用来指定文件编码为utf-8的
#a=input()               #求成绩
#a=int(a)
#if a>=90:
#   print("优秀")
#elif a>=80:
#    print("lianghao")
#elif a>=70:
 #   print("及格")
#elif a>=0:
 #   print("菜的像韩服300点的大师")

#a=input()                          求开头和结尾
#if a.startswith("a"):
 #   if a.endswith("c"):
  #    print("hello world")
   # else a.startswith("a") :
    #  print("hello")
#elif a.endswith("c"):
 #     print("world")
#else:
 #   print("caiB")

#a =int(input())          #三角形
#b =int(input())
#c =int(input())
#d=a**2
#e=b**2
#f=c**2
#if a+b>c:
 # if d+e==f :
  #   print("直角")
  #elif d+e>f:
  #   print("钝角")
  #elif d+e<f:
   # print("锐角")
#else:
 #   print("抗日7侠")

# for i in range(1,10):               # 九九乘法表
#      for j in range(1,i+1):
#             print("{}*{}={}".format(j,i,i*j),end="\t")
#      print(" ")

# for i  in range(10):               break的用法
#   if i==5:
#       break
#     else:
#         print(i)



# a=1                            #阶乘之和
# b=0
# for i in range(1,6):
#     a=a*i
#     b=b+a
# print(b)


# a=["电脑","计算机","mp3","大猪蹄子"]    #输入数字找到商品
# for i,j in enumerate(a):
#    print(i+1,j)
# i= int(input("shuru"))
# print(a[i-1])
# b=0

# for a in range(1,100):   #奇数减偶数之和
#    if  a % 2 == 0:
#        b = b -a
#    else:
#        b = b+a
# print(b)

# import random    #猜数字的次数
# a =random.randrange(1,10)
# for i in range(3):
#    b=int(input("输入数字"))
#    if b>a:
#       print("大了")
#       print("还有{}次机会".format(2-i))
#    if b<a:
#     print("小了")
#     print("还有{}次机会".format(2-i))
#    if b==a:
#      print("可以")
#      break
#
# else:
#     print("笨蛋")


# for i in range(100,1000):       #水仙花束
#      a=i//100
#      b=i//10%10
#      c=i%10
#      d=a**3+b**3+c**3
# if d==i:
#     print(i)


# a=[1,23,4,6,23,2,0]  #选择
# for i in  range(len(a)-1):
#     for j in range(i+1,len(a)):
#         if a[i] > a[j]:
#             a[i],a[j]=a[j],a[i]
#print(a)

# a=input(">>>")
# b=a.split(",")
# for i,j in enumerate(b):          # maopao
#         b[i]=int(j)            #去掉引号
# c=len(b)
# for g in range(0,c):
#     for k in range(g+1,c):
#         if b[g]>b[k]:
#              b[g],b[k]=b[k],b[g]
# print(b)

#
# a=[1,1,1,1,1,1,1]   #去重并排序      a=[1,123,,1,213,2,1,1,3,1,1]
# b=[]                                 for i in a:
# for i in a:                            if a.count(i) > 1:
#     if i not in b:                         for j in range(a.count(i)-1):
#         b.append(i)                                a.remove(i)
# b.sort()                             a.sort
# print(b)                             print(a)

#
# a=input("shurustr")          #回文
# b=len(a)
# e=b-1
# for c  in  range(b):
#     if a[c]  !=  a[-c-1]:
#           print("不是回文")
#           break
# else:
#     print("是回文")

#
# while True:             #求平均值
#     a=input(".....")
#     if a=="exit":
#         break
#     b=a.split(",")
#     c=len(b)
#     for i,j in enumerate(b):
#         b[i]=int(j)
#     print(sum(b)/c)
#     for q in b:
#         if q < sum(b)/c:
#             print(q)


# a=0                               #质数之和
# for i in range(2,100):
#     for j in range(2,i+1):
#         if i%j==0:
#             break
#     if i==j:
#         a=a+i
# print(a)

# b=1
# c=0
# a=int(input())
# for i in range(1,a+1):
#     b=b*i
#     c=b+c
# print(c)

# while True:
#     a=input()
#     b=a.split(",")
#     c=len(b)
#     for i,j  in enumerate(b):
#         b[i]=int(j)
#     d=max(b)
#     print(d)


#吧字符串变为整数
# a=input("输入")
# b=a[::1]
# d=0
# for i,j in enumerate(b):
#     for h in range(10):
#         if str(h)==j:
#             d=d+h*10**(len(a)-1-i)
# print(d)


# a=["0","1","2","3","4","5","6","7","a","b"]
# b=100
# f=""
# while  True:
#     c=b%16
#     b=b//16
#     f+=a[c]
#     if b==0:
#         break
# print(f[::-1])


# for i in range(1,1000):     #因素之和
#     i=int(i)
#     j=0
#     a=[]
#     for j in range(1,i+1):
#         j=int(j)
#         for b in range(j+1,i+1):
#             b=int(b)
#             if j*b==i:
#                 a.append(j)
#                 a.append(b)
#     if sum(a)-i==i:
#         print(i)



# for a in range(1,1000):     #因数之和
#     a=int(a)
#     sum=0
#     for b in range(1,a):
#         if a%b==0:
#             sum=sum+b
#     if sum==a:
#         print(a)




# a=[12,34,44,55,7,77,777]     #最大的放最前面，最小的放最后，其他不变
# b=a.index(max(a))
# c=a.index(min(a))
#
# a[b],a[0]=a[0],a[b]
# a[c],a[-1]=a[-1],a[c]
# print(a)

# a=int(input())
# b=int(input())
# c=int(input())
# d=a**2
# e=b**2
# f=c**2
# if a+b>c and a<c and b<c:
#     if d+e==f:
#         print("zhijiao")
#     elif d+e>f:
#         print("dunjiao")
#     elif d+e<f:
#         print("ruijiao")
# else:
#     print(77777)


# a=[12,3,12,312,3,123,213]
# #向左挪一位
# b=len(a)
# c=0
# for i in range(0,b-1):
#     c=a[i]                           #把的第一位值赋给c
#     a[i]=a[i+1]               #把后一位的值赋给前一位
#     a[i+1]=c                        #吧第一位C的值给最后一位
# print(a)                        #聪明

# a=[]                             #任意四个数组成不同的三位数
# for i in range(1,10):
#     for j in range(1,10):
#         for k in range(1,10):
#             if i!=j and j!=k and i!=k:
#                 num=100*i+10*j+k
#                 if num not in a:
#                     a.append(num)
# print(a)


# b=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]     #10进制转化16进制
# a=int(input("shuru"))
# f=""
# while True:
#     c=a%16
#     a=a//16
#     f=f+b[c]
#     if a==0:
#         break
# print(f[::-1])



# a=[12,321321,4,21,24]      #在列表中加入一位，可以准确的让他在自己的位置
# b=input("wq")
# c=b.split(",")
# for i,j in enumerate(c):
#     c[i]=int(j)
#     a.append(c[i])
#     a=list(a)
#     for h,k in enumerate(a):
#         a[h]=int(k)
#
# print(a)
#

# a=input(">>>")                #打印第一大和第二大的数字
# l=a.split(",")
# b=[]
# t=0
# for e,r in enumerate(l):
#     l[e]=int(r)
# c=len(l)
# for j in range(0,c):
#     for q in range(j,c):
#         if l[j]>l[q]:
#             t=l[j]
#             l[j]=l[q]
#             l[q]=t
# for q in l:
#   if max(l)==q:
#         print(q)
# for j in l:
#   s = l.count(l[-1])
#   if l[c - s - 1] == j:
#          print(j)



# a=input(">>>")         #任意输入四个数字组成不同的三位数
# b=a.split(",")
# t=0
# k=[]
# for i,j in enumerate(b):
#         b[i]=int(j)
# for d in range(0,i+1):
#     for f in range(0,i+1):
#         for g in range(0,i+1):
#             if b[d]!=b[f] and b[f]!=b[g] and b[d]!=b[g]:
#                 t=100*b[d]+10*b[f]+b[g]
#                 if t not in k:
#                     k.append(t)
# print(k)


# a=input(">>.")           #随机添加一位数加在正确的位置
# a=a.split(",")
# c=[21,3,214,21,3,213]
# for i in a:
#     c.append(int(i))
#     c.sort()
#    a print(c)



# 一个数加100是个完全平方数，再加168又是一个完全平方数，求这个数
# for i in range(1,85):
#     168%i==0
#     j=168/i
#     if i>j and (i+j)%2==0 and (i-j)%2==0:
#         m=(i+j)/2
#         n=(i-j)/2
#         x=n**2-100
#         print(x)

# good = [{"name":"电脑","price":399},
#         {"name":"鼠标","price":199},
#         {"name":"游艇","price":2000},
#         {"name":"佩奇","price":998},
#         {"name":"美女","price":80000},
#         {"name":"维密超模","price":1200}]
# def gd(a):
#     for n,p in enumerate(a):
#         print(n,p['name'],p['price'])
# money=int(input("你带了多少钱:"))
# while True:
#     print('余额:', money)
#     print("商品列表")
#     for n,p in enumerate(good):
#          print(n,p['name'],p['price'])
#     con=input('买东西输入任意继续，不买输入exit')
#     if con=='exit':
#         break
#     else:
#         car = []
#         while True:
#             num=input('输入商品编号:')
#             if num =='exit':
#                 break
#             else:
#                 car.append(good[int(num)])
#                 gd(car)
#                 print("输入exit退出")
#         while True:
#             print('已选购商品')
#             for n, p in enumerate(car):
#                 print(n, p['name'], p['price'])
#             move=input("删除输入del,完成输入ok")
#             if move=='del':
#                 for n, p in enumerate(car):
#                     print(n, p['name'], p['price'])
#                 moves=input('请输入编号:')
#                 car.remove(car[int(moves)])
#             elif move=='ok':
#                 break
#         while True:
#             user=input("输入ok结账")
#             sum=0
#             if user=='ok':
#                 for k,v in enumerate(car):
#                     sum+=p['price']
#                 print('消费金额',sum)
#                 if sum<money:
#                     print('购买成功')
#                     money=money-sum
#                     break
#                 else:
#                     print('余额不足请充值')
#                     moneys=int(input('输入金额:'))
#                     money+=moneys
#                     print('余额:',money)


# class Shuzi():
#     def __jiecheng(self):
#         s=1
#         d=0
#         for i in range(1,6):
#             s*=i
#             d+=s
#         return d
#     def zhishu(self):
#         a=self.__jiecheng()
#         f=0
#         for j in range(2,a+1):
#             for b in range(2,j):
#                 if j%b==0:
#                     break
#             else:
#                 f+=j
#         return f
# aaa=Shuzi()


# class bbb():
#     def __init__(self,a,b):
#         self.an=a
#         self.dd=b
#     def aa(self):
#         print('阿焦,今天吃了%i斤饭,他体重%d斤'%(self.an,self.dd))
# bb = bbb(21,222)
# bb.aa()
#

# class bbb():                  #回文
#         def aa(self):
#             a=input(">>>")
#             b=len(a)
#             c=0
#             for i in range(b):
#                 if a[i]!=a[-i-1]:
#                     print('不是回文')
#                     break
#                 else:
#                     print('是')
#                     return a
# c=bbb()
# c.aa()

# import pymysql
# abc=pymysql.connect(host='192.168.0.186',
#                 port=3306,
#                 user='root',
#                 password='123456',
#                 charset='utf8')
# #创建游标
# aaa=abc.cursor()
# aaa.execute('show databases;')
# aaa.execute('use qwe;')
# aaa.execute('show tables;')
# print(aaa.fetchall())
# with open('a.tee','w',encoding='utf-8') as q:

# aaa.execute('select * from fxs;')#执行sql语句
#print(aaa.fetchall()) #读取上一句sql语句的结果
#print(aaa.fetchmany(2))
#aaa.execute('create table biao3(姓名 char(222),年纪 int, 班级 char(23));')
# list=['小猪',1,'qwe']
# for i in range(30):
#     aaa.execute('insert into biao3   values("{}","{}","{}");'.format(list[0],list[1]+i,list[2]))
#     abc.commit()
#
# aaa.execute('select * from biao3;')
# for i in aaa.fetchall():
#       print(i)
# aaa.execute('select * from biao3;')
# a=aaa.fetchall()
# aaa.execute('desc biao3;')
# b=aaa.fetchall()
# with open('a.txt','w',encoding='utf-8') as c:
#     for i in range(len(b)):
#         c.write(b[i][0]+',')
#     for j in a:
#         c.write('\n'+'{},{},{}'.format(j[0],j[1],j[2]))
#     c.close()

#python os模式
#作用:python与操作系统之间的交互


# n=1
# w=[]
# w.append(n)
# for k in  range(1,10):
#     for i,j in enumerate(w):
#         if k<3:
#             w.append(n)
#             n+=1
#             break
#     else:
#         j=w[i]+w[i-1]
#         w.append(j)
# print(w)




