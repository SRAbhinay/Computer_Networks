import sys

# Convert an IPv4 address from dotted decimal to binary format
def ipv4_dotted_decimal_to_binary(dotted_decimal):
    # Parse the dotted decimal string into four parts
    a, b, c, d = map(int, dotted_decimal.split("."))
    
    # Convert each part to binary format
    binary = bytes([a, b, c, d])
    return binary

# Convert an IPv4 address from binary format to dotted decimal format
def ipv4_binary_to_dotted_decimal(binary):
    dotted_decimal = ".".join(str(byte) for byte in binary)
    return dotted_decimal

# Convert an IPv4 address from binary format to hexadecimal format
def ipv4_binary_to_hexadecimal(binary):
    hexadecimal = "".join("{:02x}".format(byte) for byte in binary)
    return hexadecimal

if __name__ == "__main__":
    ip_address = input("Enter an IPv4 address: ")
    
    # Get the format from the user
    format = input("Enter the format you want to convert the IP address to (binary, dottedDecimal, or hexadecimal): ")
    format = format.strip().lower()
    
    # Convert the IP address to binary format
    binary_ip = ipv4_dotted_decimal_to_binary(ip_address)

    # Convert the IP address to the requested format
    if format == "binary":
        print("Binary representation:", end=" ")
        for byte in binary_ip:
            for i in range(7, -1, -1):
                print((byte >> i) & 1, end="")
            print(".", end="")
        print()
    elif format == "dotteddecimal":
        dotted_decimal_ip = ipv4_binary_to_dotted_decimal(binary_ip)
        print("Dotted decimal representation:", dotted_decimal_ip)
    elif format == "hexadecimal":
        hexadecimal_ip = ipv4_binary_to_hexadecimal(binary_ip)
        print("Hexadecimal representation:", hexadecimal_ip)
    else:
        print("Invalid format", file=sys.stderr)
