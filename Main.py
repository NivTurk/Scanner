import tempfile
import os
import time 
import re



class OpenPort () :
    def __init__  (self):
        self.ip = "-1"
        self.port = "-1"
        
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
    
    
    
tmp_file = tempfile.NamedTemporaryFile()
os.system( 'netstat -a |awk \'{print $5}\'> %s' % tmp_file.name)
print(tmp_file.name) #file location
content = tmp_file.read()
ip_list = file_handle(content)
port_list = []
for i in ip_list:
    port_list.append(OpenPort(ip_list(i),i))
    
print(port_list)
tmp_file.close()