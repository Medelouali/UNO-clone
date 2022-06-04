import socket 
import threading

HEADER = 64
PORT = 7000
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

class Server:
    id=0
    def __init__(self, addr=ADDR):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.id = id
        self.server.bind(addr)
        self.connectedClients = []
        Server.id+=1        
    
    def start(self):
        self.server.listen()
        print(f"[LISTENING] Server is listening on {SERVER}")
        while True:
            conn, addr = self.server.accept()
            print(f"Got {addr} connected.")
            if(addr not in self.connectedClients): self.connectedClients.append(addr)
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
            
    def emit(self, msg):
        for client in self.connectedClients:
            message = msg.encode(FORMAT)
            msg_length = len(message)
            send_length = str(msg_length).encode(FORMAT)
            send_length += b' ' * (HEADER - len(send_length))
            client.send(send_length)
            client.send(message)
            # print(self.client.recv(2048).decode(FORMAT))
        
    def handle_client(self, conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")

        connected = True
        while connected:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                self.processMessage()
                print(f"[{addr}] {msg}")
                conn.send("Msg received".encode(FORMAT))

        conn.close()
        
    def processMessage(self, msg):
        if msg == "!DISCONNECT":
            # Do something crazy here
            # Better use if statements and create a function for each
            pass
        
        
        
# print("[STARTING] server is starting...")
# Server(ADDR).start()