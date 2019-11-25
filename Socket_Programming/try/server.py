'''Server program'''
import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket created")

port=1234

s.bind(('127.0.0.1',port))
print ("socket binded to port",port)

s.listen(3)
print ("Socket listening")

st='Thank you for connecting'
byt=st.encode()
while True:
	c,addr = s.accept()
	m=c.recv(1024)
	print ("Server got connection from ",addr)
	print ('Client\'s message: ',m.decode())
	c.send(byt)
	c.close() 

