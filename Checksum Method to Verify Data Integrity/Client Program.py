import socket

PORT = 8080
BUFFER_SIZE = 256

def calculate_checksum(data):
    # Initialize sum and checksum to zero
    sum = 0
    checksum = 0

    # Add all the 16-bit words together
    for i in range(0, len(data), 2):
        sum += int.from_bytes(data[i:i+2], byteorder='big')

    # Handle any odd byte at the end of the buffer
    if len(data) % 2 != 0:
        sum += int.from_bytes(data[-1:], byteorder='big')

    # Fold the sum to get a 16-bit result
    while sum >> 16:
        sum = (sum & 0xFFFF) + (sum >> 16)

    # Take the one's complement of the result
    checksum = ~sum & 0xFFFF

    return checksum

def main():
    server_ip = input("Enter server IP: ")

    # Create a socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to the server
        sock.connect((server_ip, PORT))

        # Receive data from the server
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
