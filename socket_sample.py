import socket
# create a socket:
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set up connection:
# s.connect(('www.sina.com.cn', 80))
s.connect(('www.sina.com.cn', 80))

#s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
buffer = []
while True:
    # receive data from the socket
    #d = s.recv(1024)
    d = s.recv(1024)
    if d:
        # buffer.append(d)
        buffer.append(d)
    else:
        break
s.close()
