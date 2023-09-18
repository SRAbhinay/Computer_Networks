import socket
# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name and port number
host = socket.gethostname()
port = 9999
# connect to the server
client_socket.connect((host, port))
# receive the response from the server
response = client_socket.recv(1024)
print response
# close the connection
client_socket.close()