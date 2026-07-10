import socket

HOST = socket.gethostbyname(socket.gethostname()) # dinamically getting IP, if its in virtual box then better to manually type it
print(f"Server address: {HOST}")
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # address family is an address type, and sock steam is a protocol type which is TCP
server.bind((HOST, PORT))

server.listen(5) # that number means how many unaccepted connections do we allow

while True:
    communication_socket, addr = server.accept()
    print(f"Connected to {addr}")
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"message from client is: {message}")
    communication_socket.send(f"message has been recieved!".encode('utf-8'))
    communication_socket.close()
    print(f"connection with {addr} ended!")