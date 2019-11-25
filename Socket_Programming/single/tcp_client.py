import socket,time

print('Client Side...')
time.sleep(1)

soc = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)

print(shost, '({})'.format(ip))
server_host = input('Enter server\'s address:')
name = input('Enter Client\'s name: ')
port = 1234
print('Connecting to server: {}, ({})'.format(server_host, port))
time.sleep(1)
soc.connect((server_host, port))
print("Server is Connected\n")

soc.send(name.encode())
new_client_name = soc.recv(1024)
new_client_name = new_client_name.decode()
print('{} has joined...'.format(new_client_name))
print('Enter bye to exit.')
while True:
   message = soc.recv(1024)
   message = message.decode()
   print(new_client_name, ">", message)
   message = input(str("Me > "))
   if message == "bye":
      message = "Leaving the Chat room"
      soc.send(message.encode())
      print("\n")
      break
   soc.send(message.encode())
