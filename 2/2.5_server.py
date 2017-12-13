# Echo server program
import socket
import time
import os

HOST = 'localhost'                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data : break
            if data == b'date':
                data = time.ctime()
            if data == b'os':
                data = os.name
            if data == b'ls':
                data = os.curdir
            conn.sendall(data.encode())