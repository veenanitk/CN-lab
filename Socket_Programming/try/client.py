'''client program'''
import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=1234
s.connect(('127.0.0.1',port))
msg='Hello Server'
s.send(msg.encode())
st=s.recv(1024)
print (st.decode())
s.close()
