'''TCP CLIENT SIDE PROGRAM'''

import socket
s=socket.socket()
host=socket.gethostname()
port=1235

s.connect((host,port))
rec=s.recv(1024)
print ('Received Message : '+rec.decode())
s.close()
