import socket
import threading

UDP_IP = "localhost"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def receive():
    while True:
        data, addr = sock.recvfrom(1024)
        print(data.decode())

threading.Thread(target=receive).start()

name = input("Enter your name: ")

while True:
    message = input()
    message = f"{name}: {message}"
    sock.sendto(message.encode(), (UDP_IP, UDP_PORT))
