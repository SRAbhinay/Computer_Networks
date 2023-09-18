import socket
import crcmod.predefined

PORT = 8080
BUFFER_SIZE = 256

def main():
    server_ip = input("Enter server IP: ")

    # Create a socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to the server
        sock.connect((server_ip, PORT))

        # Receive data from the server
        data = sock.recv(BUFFER_SIZE)
        received_crc = int.from_bytes(data[:4], byteorder='big')
        payload = data[4:]

        # Create a CRC object with the same polynomial used on the server
        crc32 = crcmod.predefined.Crc('crc-32')

        # Calculate CRC for received data
        crc32.update(payload)
        calculated_crc = crc32.crcValue

        # Compare calculated CRC with received CRC
        if calculated_crc == received_crc:
            print("Data integrity verified. CRCs match.")
        else:
            print("Data integrity check failed. CRCs do not match.")

if __name__ == "__main__":
    main()
