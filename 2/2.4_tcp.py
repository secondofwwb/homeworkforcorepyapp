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

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(addr)

while True:
    data = input('>')
    if not data:
        break
    tcpCliSock.send(data.encode('utf-8'))
    data = tcpCliSock.recv(bufsiz)
    if not data:
        break
    print(data.decode('utf-8'))

tcpCliSock.close()


