import socket

def check(l):
	if l[0][0] == -1 and l[0][1] == -1 and l[0][2] == -1:
		return True
	elif l[1][0] == -1 and l[1][1] == -1 and l[1][2] == -1:
		return True
	elif l[2][0] == -1 and l[2][1] == -1 and l[2][2] == -1:
		return True
	elif l[0][0] == -1 and l[1][0] == -1 and l[2][0] == -1:
		return True
	elif l[0][1] == -1 and l[1][1] == -1 and l[2][1] == -1:
		return True
	elif l[0][2] == -1 and l[1][2] == -1 and l[2][2] == -1:
		return True
	elif l[0][0] == -1 and l[1][1] == -1 and l[2][2] == -1:
		return True
	elif l[0][2] == -1 and l[1][1] == -1 and l[2][0] == -1:
		return True
	else:
		return False

s = socket.socket()
host=socket.gethostname()
port=8009
s.connect((host,port))

l = [[0 for i in range(3)] for i in range(3)]
# l = [[0,0,0],[0,0,0],[0,0,0]]
# bahut saare tareeke hote list fixed size ki banane k liye
# simple elements daal do bass badi list banani to for loop se
# for me append bhi kar sakti

while True:
	client_msg = input("First Player Move: ")
	client_msg1 = client_msg.split(" ")
	client_msg1[0] = int(client_msg1[0])
	client_msg1[1] = int(client_msg1[1])
	l[client_msg1[0]][client_msg1[1]] = -1
	if check(l) == True:
		print("First Player wins")
		client_msg = "End"
		s.send(client_msg.encode())
		break
	else:
		s.send(client_msg.encode())
	server_msg=s.recv(1024).decode()
	print("Second Player Move: ",server_msg)
	server_msg = server_msg.split(" ")
	server_msg[0] = int(server_msg[0])
	server_msg[1] = int(server_msg[1])
	l[server_msg[0]][server_msg[1]] = 1
	if(server_msg == "End"):
		print("First Player looses")
		break
	for x in l:
		print(x)

s.close()