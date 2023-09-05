import socket as S

my_name = S.gethostname()
my_ip = S.gethostbyname(my_name)

sock = S.socket(S.AF_INET, S.SOCK_STREAM)
result = sock.connect_ex((my_ip,80))
if result == 0:
    print ("Port is open")
else:
    print ("Port is not open")
sock.close()