import socket
import threading
import time

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)