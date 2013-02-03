import Engines
class Main:
    def __init__(self):
        self.running = {}
        self.stops = {}
        self.names = []
        self.threads = []
        self.res = []
        self.modulepath = "Engines."

    def ReadEngineNames(self):
        self.names.append("Engine")
        #self.names.append("Engine2")

    def StartEngines(self):
        #module= __import__("engines")
        for name in self.names:
            module= __import__("Engine")
            print globals()
            e = getattr(module,name)()
            self.threads.append(e)
            e.start()

    def Wait(self):
        for t in self.threads:
            t.join()
            tres = t.getRes()
            self.res.append(tres)
        print "All threads end"
        self.Process()

    def Process(self):
        for r in self.res:
            print r

def main():
    m = Main()
    m.ReadEngineNames()
    m.StartEngines()
    m.Wait()

if __name__ == '__main__':
    main()

    

    
