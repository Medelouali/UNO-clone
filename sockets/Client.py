import socket
import threading

HOST = "127.0.0.1"
PORT = 9090

class Client:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

    def write(self, message):
        message = message.encode('utf-8')
        self.sock.send(message)

    def stop(self):
        self.sock.close()

    def receive(self):
        while True:
            try:
                message = self.sock.recv(1024).decode('utf-8')
                print(message)
            except ConnectionAbortedError:
                break
            except:
                print("Error")
                self.socket.close()
                
client = Client(HOST, PORT)