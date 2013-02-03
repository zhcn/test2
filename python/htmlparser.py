# -*- coding: cp936 -*-
from HTMLParser import HTMLParser

class MyParser(HTMLParser):
    def handle_data(self,data):
        print data

myparser = MyParser()
myparser.feed('<dl><dt>姓名:</dt><dd><dt>城市</dt><dd>美国</dd></dl>')
s = "id=abc"
pos = s.find('id=')
print s[pos+3:]

s = "123&"

