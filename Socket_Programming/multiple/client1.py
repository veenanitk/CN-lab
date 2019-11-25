import socket 

host = socket.gethostname() 
port = 2004
BUFFER_SIZE = 2000 
MESSAGE = input("tcpClient1: Enter message/ Enter exit:") 
 
tcpClient1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClient1.connect((host, port))

while MESSAGE != 'exit':
    tcpClient1.send(MESSAGE.encode())     
    data = tcpClient1.recv(BUFFER_SIZE)
    print (" Client2:", data.decode())
    MESSAGE =input("tcpClient1: Enter message to continue/ Enter exit:")

tcpClient1.close() 
