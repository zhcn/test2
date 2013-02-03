import urllib
import urllib2
import cookielib
from HTMLParser import HTMLParser
import sys

class Node:
    def __init__(self):
        self.tag = ""
        self.attrs = []
        self.id = ""
        self.data = ""
        self.child = None
        self.parent = None
        self.nextsibling = None
        self.presibling = None
        self.finish = False

    def HaveReadStart(self):
        return self.tag!=""

    def GetSibling(self):
        self.nextsibling = Node()
        self.nextsibling.presibling = self
        self.nextsibling.parent = self.parent
        
    def GetChild(self):
        self.child = Node()
        self.child.parent = self
        

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.root = Node()
        self.cur = self.root
        self.Names = {}
        self.Ids = {}
        self.ClassNames = {}
        self.Tags = {}

    def handle_starttag(self,tag,attrs):
        #this is just test for root
        if(self.cur.HaveReadStart()==False):
            self.cur.tag = tag
            self.cur.attr = attrs
            self.SetTags(tag,self.cur)
            self.ProcessAttrs(attrs,self.cur)
        else:
            #if true should get a sibling
            if(self.cur.finish==True):
                self.cur.GetSibling()
                self.cur = self.cur.nextsibling
            #else it's a child
            else:
                self.cur.GetChild()
                self.cur = self.cur.child
            self.cur.tag = tag
            self.cur.attr = attrs
            self.SetTags(tag,self.cur)
            self.ProcessAttrs(attrs,self.cur)

    def handle_endtag(self,tag):
        #if this tag is finished, then it's the end of it's parent
        if(self.cur.finish == True):
            self.cur = self.cur.parent
        self.cur.finish = True

    def handle_data(self,data):
        self.cur.data += data

    def SetNames(self,name,node):
        if(self.Names.has_key(name)==False):
            self.Names[name] = []
        self.Names[name].append(node)

    def SetIds(self,Id,node):
        self.Ids[Id] = node

    def SetClassNames(self,cls,node):
        if(self.ClassNames.has_key(cls)==False):
            self.ClassNames[cls] = []
        self.ClassNames[cls].append(node)

    def SetTags(self,tag,node):
        if(self.Tags.has_key(tag)==False):
            self.Tags[tag] = []
        self.Tags[tag].append(node)

    def ProcessAttrs(self,attrs,node):
        for attr in attrs:
            if(attr[0]=='id'):
                self.SetIds(attr[1],node)
            elif(attr[0]=='class'):
                self.SetClassNames(attr[1],node)
            elif(attr[0]=='name'):
                self.SetNames(attr[1],node)

    def Print(self,cur,indent):
        if(cur==None):
            return
        out = ""
        for i in range(0,indent):
            out += " "
        out += cur.tag
        print out
        self.Print(cur.child,indent+4)
        out = ""
        for i in range(0,indent-1):
            out += " "
        out += "/"+cur.tag
        print out
        self.Print(cur.nextsibling,indent)

if __name__ == "__main__":
    parser = MyHTMLParser()
    parser.feed("<a id='1' ><b><e></e></b><c></c></a>")
    parser.Print(parser.root,0)
    print parser.Tags
    print parser.Names
    print parser.Ids
    print parser.ClassNames

        
        
        
