import urllib
import urllib2
import cookielib
import socket
import MyHTMLParser

class MyClient():
    def __init__(self):
        self.parser = MyHTMLParser.MyHTMLParser()
        self.timeout = 20
        socket.setdefaulttimeout(self.timeout)

    def MakeReq(self,url):
        req = urllib2.Request(url)
        return req

    def GetPage(self,url):
        req = self.MakeReq(url)
        response = urllib2.urlopen(req)
        html = response.read()
        #print html
        #html = html.decode('utf-8')
        return html

    def ParsePage(self,url):
        html = self.GetPage(url)
        html = html.lower()
        print html
        self.FindPattern(html,"wrap-bd-in bbs-list-box show clearfix")
        self.parser.feed(html)
        self.parser.Print(self.parser.root,0)

    def FindPattern(self,html,pattern):
        pos = html.find(pattern)
        print pos
        print html[pos:pos+len(pattern)]
        
        

cli = MyClient()
cli.ParsePage("http://bbs.tianya.cn")
