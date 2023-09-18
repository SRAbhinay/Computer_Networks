import socket
import crcmod.predefined
import struct

PORT = 8080
BUFFER_SIZE = 256

def main():
    # Create a socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind the socket to the specified port
        server_socket.bind(('0.0.0.0', PORT))

        # Listen for incoming connections
        server_socket.listen()

        print(f"Server listening on port {PORT}")

        # Create a CRC object with the same polynomial used on the client
        crc32 = crcmod.predefined.Crc('crc-32')

        while True:
            # Accept a connection from a client
            client_socket, client_addr = server_socket.accept()
            print(f"Accepted connection from {client_addr}")

            # Generate some data (e.g., a message)
            message = "Hello, client!"
            data = message.encode()

            # Calculate CRC for the data
            crc32.update(data)
            crc_value = crc32.crcValue

            # Prepend the CRC to the data
            data_with_crc = struct.pack('!I', crc_value) + data

            # Send data with CRC to the client
            client_socket.sendall(data_with_crc)

            # Close the connection
            client_socket.close()

if __name__ == "__main__":
    main()
