# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# a=('192.168.0.54',41)
# s.bind(a)
# s.listen(3)
# while True:
#     a,b=s.accept()
#     c=a.recv(1024)
#     print(c.decode('utf-8'))
#     reg='welcome'
#     a.send(reg.encode('utf-8'))


#udp
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
a=('192.168.0.54',233)
s.bind(a)
while True:
    a,b=s.recvfrom(1024)  #接受数据   a：客户端发送的请求数据   b:客户端的ip地址
    print(a.decode('utf-8'))
    #发送数据
    msg='welcome'
    s.sendto(msg.encode('utf-8'),b)

