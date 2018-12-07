# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# a=('192.168.0.23',333)
# s.bind(a)
# s.listen(5)
# while True:
#     a,b=s.accept()
#     msg=a.recv(1024)
#     print(msg.decode('utf-8'))
#     reg='1123123'
#     a.send(reg.encode('utf-8'))

# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# a=('0.0.0.0',333)
# s.bind(a)
# while True:
#     a,b=s.recvfrom(1024)
#     print(a.decode('utf-8'))
#     msg='qweqw'
#     s.sendto(msg.encode('utf-8'),b)
