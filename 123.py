# list
# b=int(input()).split(',')
# a =[]
# a.append(456)   #将括号中的元素添加到列表最后，只能加液一个
# print(a)
# a.insert(1,777)  #前面是下标号，后面是对应的函数，可以随意添加
# a.remove(a[2])    #删除某个元素2
# a.pop()        #删除下标位所在的元素
# print(a.index(1))   #获取某元素的下标值


# a=["电脑","计算机","mp3","大猪蹄子"]    #输入数字找到商品
# for i,j in enumerate(a):
#    print(i+1,j)
# i= int(input("shuru"))
# print(a[i-1])
# b=0
#
# for a in range(1,100):   #奇数减偶数之和
#    if  a % 2 == 0:
#        b = b -a
#    else:
#        b = b+a
# print(b)

# import random    #猜数字的次数
# a =random.randrange(1,10)
# for i in range(3):
#    b=int(input())
#    if b>a:
#       print("大了")
#       print("还有2次机会")
#    if b<a:
#     print("小了")
#     print("还有1次jihui")
#    if b==a:
#      print("可以")
#      print("0次机会")
# else:
#     print("笨蛋")


# for i in range(100,1000):       #水仙花束
#      a=i//100
#      b=i//10%1
#      c=i%10
#      d=a**3+b**3+c**3
#      if  d==i:
#         print(d)
#    a=i//100
#    b=i//10%10
#    c=i%10
#    d=a**3+b**3+c**3
#    if d==a:
# #        print(d)

# a=1
# b=0
# while  a<101:
#     b=a+b
#     a+=1
# print(b)



# a =random.randrange(1,10)   #ba for循环改为while True就可以
# i=1     #while写九九乘法表
# while i<10 :
#     j=1
#     while j<=i:
#            print("{}*{}={}".format(j,i,i*j),end="\t")
#            j=j+1
#     print(" ")
#     i+=1

# a=3
# while a>1:
#     print("hello")
#     a-=1
#     break
# else:
#     print(123)

# a=0          #质数之和
# for i in range(2,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         a=a+i
# print(a)

# a=110
# b=str(a)
# c=list(b[:])
# print(c)

#
# def prin(**x):          #可变长参数
#     a=0
#     for i in range(2,100):
#         for j in range(2,100):
#             if i%j==0 :
#                 break
#         if i==j:
#             a=a+i
#     print(a)
# prin(wqe=123,qwe=100,tr=234)


# a=[]                                  #任意四个数组成不同的三位数
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=j and j!=k and i!=k:
#                 num=100*i+10*j+k
#                 if num not in a:
#                     a.append(num)
# print(a)

# a=[1,2,34,45,56,67,78]
# b=int(input())
# a.append(b)
# a.sort()
# print(a)

# def gg():
#     a=input()
#     a=a.split(",")
#     a=set(a)
#     a=list(a)
#     b=[]
#     for i in a:
#         if i not in b:
#             b.append(i)
#     for e,f in enumerate(b):
#         b[e]=int(f)
#     print(b)
# gg()

# a=123
# def aaa():
#     global a
#     a=1234
#     print(a)
#     return a
# print(aaa()+123)
# aaa()

# aa=lambda x,y:x + y
# print(aa(3,4))

# b=[x for x in range(100) if x < 90]
# print(b)


# a=["{}*{}={}".format(i,j,i*j)for i in range(1,10) for j in range(1,i+1)]  #列表推导式
# prin(a)



# a=open(r'C:\Users\zhang\Desktop\b.txt','w',encoding='utf-8')
# for f in range(1,11):
#     for i in range(1,10):
#         for j in range(1,i+1):
#             a.write(" {}*{}={} ".format(i,j,i*j))
#         a.write(" \n")
# a.close()
#
#
#
#
# a=open(r'C:\Users\zhang\Desktop\a.txt','w',encoding='utf-8')
# for f in range(1,11):
#     for i in range(1,10):
#         for j in range(1,i+1):
#             a.write(" {}*{}={} ".format(i,j,i*j))
#         a.write(" \n")
# a.close()
#









# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}*{}={}".format(i,j,i*j),end="\t")
#     print()

# def aa(x=2):
    # a=0
    # for i in range(x,100):
#         for j in range(2,i):
#             if i%j == 0:
#                 break
#         else:
#              a=a+i
#     print(a)
# aa()
#
# c=open('a.txe','w',encoding='utf-8')
# c.write('trywtdyadwhde')
# c.close()
#
# goods=[{"name":"电脑","price":399},
#        {"name":"游艇","price":2000},
#        {"name":"佩奇","price":9928},
#        {"name":"美女","price":80000}]
# b=int(input("你带多少现金"))
# for i,j in enumerate(goods):
#     print(i,j["name"],j["price"])
# a=input("买东西吗，输入exit不买")
# while True:
#     if a=="exit":
#         break
#     else:
#         car=[]
#         while True:
#             c = input("买啥,穷逼")
#             if c=='exit':
#                 break
#             else:
#                 car.append(goods[int(c)])
#                 print('输入exit退出')
#     while True:
#             for d,f in enumerate(car):
#                 print(f["name"],f["price"])
#             q=input("退货del，买完了输OK")
#             if q=="del":
#                     gg =int(input('请输入编号:'))
#                     car.remove(car[gg])
#                     print(car[int(c)])
#             elif q=="ok":
#                     break
#     w=input("输入ok结账")
#     sum=0
#     if w == 'ok':
#             for k,v in enumerate(car):
#                     sum+=f['price']
#                     print('消费金额',sum)
#             if sum<=b:
            #        print('购买成功')
            #         b=b-sum
            #         break
            # else:
            #         print('余额不足请充值')
            #         r=int(input('输入金额:'))
            #         b+=r
            #         print('余额:',b)


# def aaa():
#    for a in range(1,10):
#        for b in range(1,a+1):
#            print('{}*{}={}'.format(b,a,a*b),end='\t')
#        print()
# aaa()


# class aaa():
#     def aa(self,a):
#         a+=2
#         return a
# b=aaa()
# print(b.aa(2))
#
# import random
# lan=random.randrange(1,17)
# a=[]
# for i in range(6):
#     hong =random.randrange(1,34)
#     a.append(hong)
# a.sort()
# print(a)



#
# for a in range(1,1000):     #因数之和
#     a=int(a)
#     sum=0
#     for b in range(1,a):
#         if a%b==0:
#             sum=sum+b
#     if sum==a:
#         print(a)




