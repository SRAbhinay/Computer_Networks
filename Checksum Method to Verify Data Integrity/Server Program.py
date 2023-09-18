import socket
import struct

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
    # Create a socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind the socket to the specified port
        server_socket.bind(('0.0.0.0', PORT))

        # Listen for incoming connections
        server_socket.listen()

        print(f"Server listening on port {PORT}")

        while True:
            # Accept a connection from a client
            client_socket, client_addr = server_socket.accept()
            print(f"Accepted connection from {client_addr}")

            # Generate some data (e.g., a message)
            message = "Hello, client!"
            
            # Calculate checksum for the data
            data = message.encode()
            checksum = calculate_checksum(data)

            # Prepend the checksum to the data
            data_with_checksum = struct.pack('!H', checksum) + data

            # Send data with checksum to the client
            client_socket.sendall(data_with_checksum)

            # Close the connection
            client_socket.close()

if __name__ == "__main__":
    main()
