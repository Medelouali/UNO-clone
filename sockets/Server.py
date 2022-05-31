
from socket import *
# Port number of server
server_port = 9090
# Server using IPv4 and UDP socket
server_socket = socket(AF_INET, SOCK_DGRAM)
# Bind server to port number and IP address
server_socket.bind(("127.0.0.2", server_port))
print("The server is ready to receive msg...")
while True:
    # Extract message and client address from received msg
    message, client_address = server_socket.recvfrom(2048)
    # Create response message
    modified_message = message.upper()
    server_socket.sendto(modified_message, client_address)