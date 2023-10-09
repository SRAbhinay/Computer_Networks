import socket

PORT = 8080
BUFFER_SIZE = 256

def calculate_checksum(data):
    sum = 0
    checksum = 0

    for i in range(0, len(data), 2):
        sum += int.from_bytes(data[i:i+2], byteorder='big')

    if len(data) % 2 != 0:
        sum += int.from_bytes(data[-1:], byteorder='big')

    while sum >> 16:
        sum = (sum & 0xFFFF) + (sum >> 16)

    checksum = ~sum & 0xFFFF

    return checksum

def main():
    server_ip = input("Enter server IP: ")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((server_ip, PORT))

        data = sock.recv(BUFFER_SIZE)
        received_checksum = int.from_bytes(data[:2], byteorder='big')
        payload = data[2:]

        # Calculate checksum for received data
        calculated_checksum = calculate_checksum(payload)

        # Compare calculated checksum with received checksum
        if calculated_checksum == received_checksum:
            print("Data integrity verified. Checksums match.")
        else:
            print("Data integrity check failed. Checksums do not match.")

if __name__ == "__main__":
    main()
