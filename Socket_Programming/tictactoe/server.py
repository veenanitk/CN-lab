import socket

def check(l):
	if l[0][0] == 1 and l[0][1] == 1 and l[0][2] == 1:
		return True
	elif l[1][0] == 1 and l[1][1] == 1 and l[1][2] == 1:
		return True
	elif l[2][0] == 1 and l[2][1] == 1 and l[2][2] == 1:
		return True
	elif l[0][0] == 1 and l[1][0] == 1 and l[2][0] == 1:
		return True
	elif l[0][1] == 1 and l[1][1] == 1 and l[2][1] == 1:
		return True
	elif l[0][2] == 1 and l[1][2] == 1 and l[2][2] == 1:
		return True
	elif l[0][0] == 1 and l[1][1] == 1 and l[2][2] == 1:
		return True
	elif l[0][2] == 1 and l[1][1] == 1 and l[2][0] == 1:
		return True
	else:
		return False

s=socket.socket()
host=socket.gethostname()
port=8009

s.bind((host,port))
s.listen(1)
c,addr=s.accept()

# l = [[0 for i in range(3)] for i in range(3)]
l = [[0,0,0],[0,0,0],[0,0,0]]
print("Enter moves: row(0,2) column(0,2")

while True:
	client_msg = c.recv(1024).decode()
	if(client_msg == "End"):
		print("Second Player looses")
		break
	print("First Player Move: ",client_msg)
	client_msg = client_msg.split(" ")
	client_msg[0] = int(client_msg[0])
	client_msg[1] = int(client_msg[1])
	l[client_msg[0]][client_msg[1]] = -1
	server_msg = input("Second Player Move: ")

	# list object can't be send so creating a new list and sending only string	
	server_msg1 = server_msg.split(" ")
	server_msg1[0] = int(server_msg1[0])
	server_msg1[1] = int(server_msg1[1])
	l[server_msg1[0]][server_msg1[1]] = 1
	for x in l:
		print(x)

	if check(l) == True:
		print("Second Player wins")
		server_msg = "End"
		c.send(server_msg.encode())
		break
	else:
		c.send(server_msg.encode())

s.close()