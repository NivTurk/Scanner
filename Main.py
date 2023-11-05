import tempfile
import os
import time 
import re



class OpenPort () :
    def __init__  (self, ip_val, port_val):
        self.ip = ip_val
        self.port = port_val

    def __str__(self):
        return str("ip: " + str(self.ip)+" port: "+str(self.port))
    def __repr__(self):
        return str(self)    
    def setip (self,addr):
        if isip(addr):
            self.ip = addr
    
    def getip (self):
        return self.ip
    def setport (self,num):
        if isport(num):
            self.port = num
    def getport(self):
        return self.port
    def _ip_and_port(self):
        str = self.getip()
        str+= ','
        str += self.getport()
        return str
    
        
        
        
def isip (addr):
    count =0
    for i in range (addr.length -1):
        if count ==3:
            print ("illegal IP: %s" %addr)
            return False
        if addr[i].isnumeric():
            count +=1
        if addr[i] == '.':
            count = 0
        if i == addr.length and addr[i] == ':':
            return True
        else:
            print("illegal IP: %s" %addr)
            return False

def isport (num):
    if num >=0 or num <= 65365:
        return 0
    else:
        print ('Wrong port')
        return 0

def file_handle(tmp_file):
    tmp  = "STREAM stream STREAM"
    TARGET = "(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
    list = re.findall(TARGET,str(tmp_file))
    return list
    
    
tst = OpenPort("addr" , "port")
print("test ->" )
print(tst)

tmp_file = tempfile.NamedTemporaryFile()
os.system( 'netstat -a |awk \'{print $5}\'> %s' % tmp_file.name)
print(tmp_file.name) #file location
content = tmp_file.read()
ip_list = file_handle(content)
port_list = []
j=0
for i in ip_list:
  tmp = OpenPort(i,str(j))
  port_list.append(tmp)
  j+=1
print (ip_list)
# print("\n\n\n")   
print(port_list)
tmp_file.close()