# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        input_data = input('>')
        if input_data is not '':
            break
        else:
            print('please input command')
    s.sendall(input_data.encode())
    data = s.recv(1024)
print('Received', repr(data))