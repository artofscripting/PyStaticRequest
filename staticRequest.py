import hashlib 
import os 
import os.path
import urllib.request as ur
import ssl

class staticRequest:
   url = str()
   file = str()
   filename = str()
   text = str()
   def __init__(self,url):
      isdir = os.path.isdir("data")
      if not (isdir):
         os.mkdir("data") 
      result = hashlib.md5(url.encode()) 
      self.url = url
      self.filename = result.hexdigest()
      self.file =os.path.join("data", self.filename)
      pathExists = os.path.exists(self.file)
      if not pathExists:
         with open(os.path.join("data", "key.csv"), 'a') as the_file:
            the_file.write( self.filename + "," + self.url )           
         self.updateRequest()
      else:
         with open(self.file, 'r') as file:
            data = file.read()
             
         self.text = data
   def clearRequest(self):
      try:
         os.remove(self.file)  
      except:
         do = 0
   def updateRequest(self, userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36', headers = False ):
      self.clearRequest()
      ctx = ssl.create_default_context()
      ctx.check_hostname = False
      ctx.verify_mode = ssl.CERT_NONE  
      if headers == False:  
         req = ur.Request(
             self.url, 
             data=None, 
             headers={
                 'User-Agent': userAgent
             }
         )
      else:
         req = ur.Request(
             self.url, 
             data=None, 
             headers=headers
         )         
      
      
      
      
      
      s = ur.urlopen(req, context=ctx)
      sl = s.read()
      self.text = sl.decode("utf-8")
      with open(self.file, 'a') as the_file:
         the_file.write( sl.decode("utf-8") )  
         
      
         
#myreq = staticRequest("http://artofscripting.com")
#myreq.clearRequest()
#print(myreq.text)
      
    
   