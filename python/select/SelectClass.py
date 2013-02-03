import threading
import socket
import select

class Select(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.host = "10.10.129.93"
        self.port = 50006
        self.addr = (self.host,self.port)

    def func(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind(self.addr)
        s.listen(5)
        print "beginning ..."
        while(True):
            fds = select.select([s,],[],[])
            infds = fds[0]
            if(len(infds)!=0):
                conn,addr = infds[0].accept()
                print addr
                while(True):
                    fds = select.select([conn,],[],[])
                    flist = fds[0]
                    if(len(flist)!=0):
                        buf = flist[0].recv(1024)
                        print buf
                
    def run(self):
        self.func()

def main():
    t = Select()
    t.start()
    t.join()

if __name__ == '__main__':
    main()
