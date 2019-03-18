from socket import *

s = socket(AF_INET, SOCK_STREAM)

s.connect(('localhost', 7777))
s.send('Hello, world'.encode())

data = s.recv(1024)
print (data.decode())

s.close()
