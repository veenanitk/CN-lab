'''UDP CLIENT SIDE PROGRAM'''

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host='127.0.0.1'
port=1235

msg=' '
s.sendto(msg.encode(),(host,port))
data,addr=s.recvfrom(1024)
print ('Message received from server: ',addr)
print ('Received Message : ',data.decode())

