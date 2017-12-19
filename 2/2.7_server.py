import socket


HOST = 'localhost'
PORT = 50007
socket_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_s.bind((HOST, PORT))
socket_s.listen(1)

while True:
    print('-----server start------')
    conn, addr = socket_s.accept()
    print('accept connet from:', addr)
    print('-----wait message------')

    while True:
        rec_data = conn.recv(1024)
        print('Received', rec_data.decode())
        send_data = input('>')
        conn.sendall(send_data.encode())