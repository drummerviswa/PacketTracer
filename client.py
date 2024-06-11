import socket
from pickle import dumps,loads

x=socket.socket()
port,host=5000,'127.0.0.1'
x.connect((host,port))
ch=""
while(ch!="#"):
	print("Send data:")
	data=input()
	ch=data
	x.sendall(dumps(data))
