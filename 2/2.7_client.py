# Echo client program
import socket

HOST = 'localhost'
PORT = 50007
socket_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_c.connect((HOST, PORT))

while True:
    input_data = input('>')
    socket_c.sendall(input_data.encode())
    data = socket_c.recv(1024)
    print('Received', data.decode())