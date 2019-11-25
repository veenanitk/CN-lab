import socket,time

print('Server Side')
time.sleep(1)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
port = 1234
s.bind((host_name, port))
print(host_name, '({})'.format(ip))
name = input('Enter Server\'s name: ')
client_name,addr=s.recvfrom(1024)
client_name=client_name.decode()
print('{} has joined...'.format(client_name))
s.sendto(name.encode(),addr)
print('Enter bye to exit.')
while True:
	message = input('Me > ')
	if message == 'bye':
		message = 'Bye Bye'
		sent1=s.sendto(message.encode(),addr)
		print("\n")
		break
	sent1=s.sendto(message.encode(),addr)
	msg,ad=s.recvfrom(1024)
	msg=msg.decode()
	print(client_name, '>', msg)
