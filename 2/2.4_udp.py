from socket import *

hostname = input("input hostname (default localhost):")
port = input("input port (default 21567):")



if hostname == '':
    hostname = 'localhost'

if port == '':
    port = 21567
else:
    port = int(port)

bufsiz = 1024
addr = (hostname, port)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('>')
    if not data:
        break
    udpCliSock.sendto(data.encode(), addr)
    data, addr = udpCliSock.recvfrom(bufsiz)
    if not data:
        break
    print(data.decode('utf-8'))

udpCliSock.close()



