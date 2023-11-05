import socket as sok
import threading  as trd

sock = sok.socket(sok.AF_INET,sok.SOCK_STREAM)

sock.bind (('0.0.0.0', 10000))

sock.listen(1)
connections = []
def handle_connections(c, a):
    global connections
    while True:
        data = c.recv(1024)
        for connection in connections:
            connection.send(bytes(data))
        if not data or data == ('bye'):
            connections.remove(c)
            c.close()
            break


while True:
    c, a = sock.accept() 
    print("here")
    cThread = trd.Thread(target = handle_connections, args = (c , a))
    cThread.daemon=True
    cThread.start()
    connections.append(c)
    print(connections)

