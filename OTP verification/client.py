import socket

def verify_otp(otp, user_input):
    return otp == user_input

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

received_otp = client_socket.recv(1024).decode()
user_input = input("Enter the OTP you received: ")

if verify_otp(received_otp, user_input):
    print("OTP verification successful.")
else:
    print("OTP verification failed.")

client_socket.close()
