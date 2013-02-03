import socket
import select

host = "10.10.129.93"
port = 50000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)
print "beginning ..."
while True:
    fds = select.select([s,],[],[])
    infds = fds[0]
    if(len(infds)!=0):
        conn,addr = s.accept()
        print addr
