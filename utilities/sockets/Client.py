
import socket
# from Server import Server

HEADER = 64
CLIENT_PORT = 7001 
SERVER_PORT = 7000 
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

CLIENT_CLIENT="192.168.0.152"
CLIENT_SERVER="192.168.0.151"

ADDR = (CLIENT_SERVER, SERVER_PORT)

class Client:
    def __init__(self, addr=ADDR):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(addr)
        
    def send(self, msg):
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)
        print(self.client.recv(2048).decode(FORMAT))
        
    def test(self):
        self.send(input(">>> "))
        self.send(input(">>> "))
        self.send(input(">>> "))
        self.quit()
        
    def start(self):
        self.server.start()
        
    def receive(self):
        self.start()
        
    def quit(self):
        self.send(DISCONNECT_MESSAGE)
        
# Client().test()