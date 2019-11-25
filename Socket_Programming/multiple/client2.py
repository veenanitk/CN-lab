import socket 

host = socket.gethostname() 
port = 2004
BUFFER_SIZE = 2000 
MESSAGE = input("tcpClient2: Enter message/ Enter exit:")
 
tcpClient2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClient2.connect((host, port))

while MESSAGE != 'exit':
    tcpClient2.send(MESSAGE.encode())     
    data = tcpClient2.recv(BUFFER_SIZE)
    print (" Client1:", data.decode())
    MESSAGE = input("tcpClient2: Enter message to continue/ Enter exit:")

tcpClient2.close() 


