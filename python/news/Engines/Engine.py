import threading

class Engine(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def func(self):
        print "Engine"

    def run(self):
        self.func()
        self.res = "test"

    def getRes(self):
        return self.res
