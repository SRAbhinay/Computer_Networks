import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name and port number
host = socket.gethostname()
port = 9999

# Bind the socket to a public host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)
print('Server running...')

while True:
    # Establish a connection
    client_socket, address = server_socket.accept()
    print("Got a connection from %s" % str(address))

    # Send a thank you message to the client
    message = "Thank you for connecting"
    client_socket.send(message.encode())  # Encode the message to bytes before sending

    # Close the connection
    client_socket.close()
