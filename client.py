import socket

'''
because we are using same device we just specify same ip address for the server
if we have like another device and we are connected to the local network then type private ip address of a targeted server
if we are running it through the internet then we use public ip address, u can get it from website like 'myip.is'
'''
#HOST = 'target-ip'
HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send("Hello World!".encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))
