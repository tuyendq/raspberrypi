import socket
import sys

# Create socket AF_INET: Address Family Internet
# SOCKET_STREAM -> TCP connection
try:
	mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
	print("Failed to create socket")
	sys.exit()
# Get IP address of www.google.com
try:
	host = socket.gethostbyname("www.google.com")
except socket.gaierror:
	print("Failed to get host")
	sys.exit()
# Connect to host
mysocket.connect((host, 80))

# Send data on a socket
message = "GET / HTTP/1.1\r\n\r\n"
try:
	mysocket.sendall(message)
except socket.error:
	print("Failed to send")
	sys.exit()
# Receive data on a socket
data = mysocket.recv(1000)
print(data)
# Close a socket
mysocket.close()
