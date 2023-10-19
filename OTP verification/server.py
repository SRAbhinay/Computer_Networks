import socket
import random

def generate_otp():
    return str(random.randint(1000, 9999))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

print("Server listening on port 12345")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    otp = generate_otp()
    print(f"Generated OTP: {otp}")

    client_socket.send(otp.encode())
    client_socket.close()
