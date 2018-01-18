import socket
import hashlib
'''
程序未完成
'''

HOST = 'localhost'
PORT_server = 50007

list_flag = {}

def save_client(data,addr,list_flag):
    host = addr[1]
    port = addr[2]
    string_flag = str(host)+str(port)
    flag = hashlib.md5(string_flag.encode())
    # username = data.decode()
    dict = {'host':host, 'port':port, 'flag':flag}
    list_flag[flag] = dict
    print('new user online')


if __name__ == '__main__':
    print('------start server-----')
    socket_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_s.bind((HOST, PORT_server))
    print('---waiting for message---')
    while True:
        data, addr = socket_s.recvfrom(1024)
        if data.decode() == 'on1line':
            save_client(data,addr,list_flag)
        if data.decode() == 'touser+username':


        socket_s.sendto(data2, addr2)





