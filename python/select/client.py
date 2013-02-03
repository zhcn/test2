import socket
from time import sleep,ctime

host = "10.10.129.93"
port = 50006
addr = (host,port)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(addr)
i = 0
while True:
    i = i+1
    s.send("%d"%i)
    print "send",i
    sleep(1)
