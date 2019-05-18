import socket
import sys

# Create a socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an IP address and port
try:
	mysock.bind (("", 1234)) # "" means receive from ANY host
except socket.error:
	print("Failed to bind")
	sys.exit()
# Listen for a connection
mysock.listen(5) # baglog is 5

#Accept the connection
while True:
	conn, addr = mysock.accept()

# Receive the request
	data = conn.recv(1000)
	if not data:
		break
	conn.sendall(data)

conn.close()

# Send the response


mysock.close()
