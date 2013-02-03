01.import urllib.request  
02.import urllib.parse  
03.import http.cookiejar  
04.  
05.class LoginRenren():          
06.    def __init__(self):  
07.        """log in www.renren.com"""  
08.        #self.origURL = "http://www.renren.com/home"   
09.        #self.domain = "renren.com"   
10.        self.log_url = "http://www.renren.com/PLogin.do"  
11.        self.cj = http.cookiejar.CookieJar()  
12.        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj))  
13.        urllib.request.install_opener(self.opener) #Installing an opener is only necessary if you want urlopen to use that opener         
14.  
15.    def login(self, email, password):  
16.        self.email = email  
17.        self.password = password  
18.        params = {"email":self.email, "password":self.password}#, "origURL":self.origURL, "domain":self.domain}   
19.        params = urllib.parse.urlencode(params)  
20.        params = params.encode('utf-8')   
21.        #response = self.opener.open(self.log_url,params)   
22.        response = urllib.request.urlopen(self.log_url, params)  
23.        file = open("d:\\renren.html", "wb")  
24.        file.write(response.read())  
25.  
26.def login(email = "myemail@163.com", password = "mypassword" ):      
27.    renren = LoginRenren()  
28.    renren.login(email, password)  
