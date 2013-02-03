#-*- coding:utf-8 -*-
s = u'哈哈'
print s
f = open("d:/test.txt",'w')
#print s.encode('utf8')
f.write(s.encode("utf8"))
#f.write(s)
f.close()
