import socket,time

print('Client Side...')
time.sleep(1)

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, '({})'.format(ip))
#server_host = input('Enter server\'s address:')
name = input('Enter Client\'s name: ')
port = 1234
soc.sendto(name.encode(),(shost,port))

server_name,addr=soc.recvfrom(1024)
server_name=server_name.decode()

print('{} has joined...'.format(server_name))
print('Enter bye to exit.')
while True:
   message,ad = soc.recvfrom(1024)
   message = message.decode()
   print(server_name, ">", message)
   message = input(str("Me > "))
   if message == "bye":
      message = "Leaving the Chat room"
      soc.sendto(message.encode(),ad)
      print("\n")
      break
   soc.sendto(message.encode(),ad)
