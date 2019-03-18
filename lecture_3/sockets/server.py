from socket import *

s = socket(AF_INET, SOCK_STREAM)

s.bind(('localhost', 7777))
s.listen(1)

(conn, addr) = s.accept()

while True:
    data = conn.recv(1024)
    print(data.decode())

    if not data: 
        break

    conn.send('Hello'.encode())

conn.close()
