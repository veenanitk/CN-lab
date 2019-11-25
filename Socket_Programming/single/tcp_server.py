import socket,time

print('Server Side')
time.sleep(1)

soc = socket.socket()
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
port = 1234
soc.bind((host_name, port))
print(host_name, '({})'.format(ip))
name = input('Enter Server\'s name: ')

soc.listen(1)
print('Waiting for connections...')
connection, addr = soc.accept()

client_name = connection.recv(1024)
client_name = client_name.decode()
print(client_name + ' has connected.')
print('Press bye to leave the chat room')
connection.send(name.encode())
while True:
   message = input('Me > ')
   if message == 'bye':
      message = 'Bye Bye'
      connection.send(message.encode())
      print("\n")
      break
   connection.send(message.encode())
   message = connection.recv(1024)
   message = message.decode()
   print(client_name, '>', message)
