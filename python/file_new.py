import urllib
import urllib2  
#import urllib.parse  
import cookielib
  
class LoginRenren():          
    def __init__(self):  
        """log in www.renren.com"""     
        self.log_url = "http://www.renren.com"  
        #self.cj = cookielib.LWPCookieJar()  
        #self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))  
        #urllib2.install_opener(self.opener) #Installing an opener is only necessary if you want urlopen to use that opener         
  
    def login(self, email, password):  
        #self.email = email  
        #self.password = password  
        #params = {"email":self.email, "password":self.password}#, "origURL":self.origURL, "domain":self.domain}   
        #params = urllib.urlencode(params)  
        #params = params.encode('utf-8')
        params = ""
        req = urllib2.Request(self.log_url)
        cookiefile = open("d:\\cookies.txt","r")
        cookie = cookiefile.read()
        print cookie
        req.add_header('Cookie',cookie)
        response = urllib2.urlopen(req, params)  
        #print response.read()
        file = open("d:\\renren.html", "wb")  
        file.write(response.read())  
  
def login(email = "", password = "" ):      
    renren = LoginRenren()  
    print "logging in "
    renren.login(email, password)

login()
