'''TCP CLIENT'''
import socket
s=socket.socket()
host=socket.gethostname()
port=1245

s.connect((host,port))

msg='What is the date today?'

s.send(msg.encode())
data_received=s.recv(1024)
print ('Today\'s date is : ',data_received.decode())
