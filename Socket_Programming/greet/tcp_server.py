'''TCP SERVER SIDE PROGRAM'''

import socket
s=socket.socket()
host=socket.gethostname()
port=1235

s.bind((host,port))

print ('Waiting for connection')
s.listen(5)

msg='Hello Client'
while True:
	c,addr = s.accept()
	print ('Connection from ',addr)
	c.send(msg.encode())
	c.close()
