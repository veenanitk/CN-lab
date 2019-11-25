'''SERVER SIDE - UDP'''
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print ('Socket created')
udp_host='127.0.0.1'
udp_port=1235

s.bind((udp_host,udp_port))
print ('Socket binded to port',udp_port)

st='Hi Client'
while True:
	c,addr = s.recvfrom(1024)
	print ('Connected to ',addr)
	sent=s.sendto(st.encode(),addr)
	print ('Message sent to client')
