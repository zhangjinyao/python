#tcp
# import socket
# sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #连接服务器  接受的参数也是元祖
# sock.connect(('192.168.0.54',41))
# aaa='n hao'
# sock.send(aaa.encode('utf-8'))
# msg=sock.recv(1024)
# print(msg.decode('utf-8'))

#udp
# import socket
# #创建socket  封装协议
# sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #发送数据请求
# a=('192.168.0.54',233)
# reg='买了否冷'
# sock.sendto(reg.encode('utf-8'),a)
# #接受响应
# c=sock.recv(1024)
# print(c.decode('utf-8'))
