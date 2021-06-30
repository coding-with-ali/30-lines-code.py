# importing socket module
import socket

# getting machine name
hostname = socket.gethostname()

# getting IP Address
IPAddr = socket.gethostbyname(hostname)

# printing hostname
print("Your Computer Name is:" + hostname)

# printing IP Address
print("Your Computer IP Address is:" + IPAddr)