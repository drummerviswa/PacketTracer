import socket
from pickle import dumps,loads
import threading

def recv_from_client(con,addr):
	global connected
	while(connected):
		data=con.recv(1024)
		print(f'Recieved from clients {addr[1]}:',loads(data))
		
x=socket.socket()
port,host=5000,'127.0.0.1'
n=int(input("No.of client:"))
x.bind((host,port))
x.listen(2)
clients=[]
i=0
while i<n:
	con,addr=x.accept()
	clients.append((con,addr))
	print("Client connected",addr)
	i+=1
connected=True
active_threads=[]
for x in clients:
	t=threading.Thread(target=recv_from_client,args=x)
	t.start()
	active_threads.append(t)
