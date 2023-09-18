import socket
import threading
import time

UDP_IP = "localhost"
UDP_PORT = 5005

clients = {}

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

def handle_client():
    while True:
        data, addr = sock.recvfrom(1024)
        if addr not in clients:
            clients[addr] = data.decode().split(":")[0]
            print(f"{clients[addr]} connected")
        else:
            message = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {data.decode()}"
            print(message)
            for client_addr in clients:
                if client_addr != addr:
                    sock.sendto(message.encode(), client_addr)

threading.Thread(target=handle_client).start()
