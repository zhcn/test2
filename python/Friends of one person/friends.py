import urllib
import urllib2
import cookielib
from HTMLParser import HTMLParser
import sys
import codecs


class TestParser(HTMLParser):
    def handle_data(self,data):
        print data

class FriendListParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.pagenum = 0
        self.FindOneList = False
        self.FindOnePerson = False
        self.FindDt = False
        self.FindDd = False
        self.info = []
        self.personid = 0

    def setFile(self,f):
        self.file = f
    
    def handle_starttag(self,tag,attrs):
        if(tag=='ol'):
            print "Start tag:",tag
            for attr in attrs:
                if(attr[1]=='friendListCon'):
                    self.FindOneList = True
                    print "\t attr:",attr
        elif((tag=='div' and attrs[0][1]=='info')and self.FindOneList==True):
            self.FindOnePerson = True
        elif(tag=='dt'):
            self.FindDt = True
        elif(tag=='dd'):
            self.FindDd = True
        elif(tag=='a' and self.FindDd==True):
            href = attrs[0][1]
            pos = href.find("id=")
            if(pos!=-1):
                self.personid = href[pos+3:]
                #print "person id:",personid

    def handle_endtag(self,tag):
        if(tag=='ol'):
            self.FindOneList = False
        elif(tag=='div' and self.FindOnePerson==True):
            self.FindOnePerson = False
            #print self.info
            for data in self.info:
                print data
                data = data +u'\t'
                self.file.write(data.encode("utf-8"))
            print "person id:",self.personid
            data = u"person id\t"+self.personid+u"\n"
            self.file.write(data.encode("utf-8"))
            print
            self.info=[]
        elif(tag=='dt'):
            self.FindDt = False
        elif(tag=='dd'):
            self.FindDd = False

    def handle_data(self,data):
        if(self.FindDt == True or self.FindDd == True):
            #print data
            if(len(data.strip())!=0):
                self.info.append(data)

class GetFriends():
    def __init__(self):
        self.listurl = 'http://friend.renren.com/GetFriendList.do?id='
        self.cookie = self.GetCookie()
        self.queue = []
        self.map = {}
        self.parser = FriendListParser()

    def GetCookie(self):
        cookiefile = open("d:/cookies.txt","r")
        cookie = cookiefile.read()
        return cookie

    def MakeReq(self,url):
        req = urllib2.Request(url)
        req.add_header('Cookie',self.cookie)
        #req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; rv:15.0) Gecko/20100101 Firefox/15.0.1')
        return req

    def GetNumOfPage(self,html):
        pos1 = html.rfind("curpage=")
        pos2 = html.rfind("&amp;id=")
        print pos1,pos2
        return int(html[pos1+len('curpage='):pos2])

    def GetName(self,html,personid):
        s = '<a href="http://www.renren.com/profile.do?id='+personid+'">'
        pos1 = html.find(s)
        pos2 = html.find('</a>',pos1)
        return html[pos1+len(s):pos2]
    
    def FriendsOfSome(self,personid):
        req = self.MakeReq(self.listurl+personid)
        response = urllib2.urlopen(req)
        html = response.read()
        self.name = self.GetName(html,personid)
        self.name = self.name.decode("utf-8")
        self.file = open("d:/profiles/"+self.name+".txt","w")
        self.file.write(codecs.BOM_UTF8)
        self.parser.setFile(self.file)
        self.numofpage = self.GetNumOfPage(html)
        print self.numofpage
        for i in range(1,self.numofpage+2):
            self.ParseFriendListPage(html.decode('utf-8'))# utf-8
            if(i<=self.numofpage):
                req = self.MakeReq(self.listurl+personid+"&curpage="+str(i))
                response = urllib2.urlopen(req)
                html = response.read()
                i = i+1

    def Pop(self):
        personid = self.queue.pop(0)
        self.map.pop(personid)
        return personid

    def Insert(self,personid):
        if(self.map.has_key(personid)):
            return False
        self.queue.append(personid)
        self.map[personid] = 1
        return True

    def ParseFriendListPage(self,response):
        self.parser.feed(response)

    def Search(self):
        print 'Start searching'
        while(len(self.queue)):
            personid = self.Pop()
            self.FriendsOfSome(personid)
        self.file.close()
        print 'Search finished'


getfriends = GetFriends()
getfriends.Insert('236983824')
getfriends.Search()
