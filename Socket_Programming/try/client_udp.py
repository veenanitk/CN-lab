'''CLIENT SIDE - UDP'''
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_host='127.0.0.1'
udp_port=1235

msg='Hi Server'
s.sendto(msg.encode(),(udp_host,udp_port))
data,addr = s.recvfrom(1024)
print ('Message received from server: ',addr)
print ('Message received from server is : ',data.decode())
s.close()

