import tempfile
import os
import time 


tmp_file = tempfile.NamedTemporaryFile()
os.system( 'netstat > %s' % tmp_file.name)
print(tmp_file.name) #file location
print(tempfile.gettempdir())
tmp_file.seek(0)
time.sleep(60)
tmp_file.close()