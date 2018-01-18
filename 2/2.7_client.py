# Echo client program
import socket


HOST = 'localhost'
PORT_client = 50007



if __name__ == '__main__':
    socket_c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        send_data = input('>')
        socket_c.sendto(send_data.encode(), (HOST, PORT_client))