'''TCP SERVER SIDE'''
import socket
from datetime import date
s=socket.socket()
host=socket.gethostname()
port=1245

Date=date.today()
m= str.encode(Date.strftime("%d/%m/%Y"))
s.bind((host,port))
s.listen(5)

while True:
	c,addr = s.accept()
	val=c.recv(1024)
	print ('Got connection from: ',addr)
	print ('Cient\'s meassage: ',val.decode())
	c.sendall(m)
	c.close()
