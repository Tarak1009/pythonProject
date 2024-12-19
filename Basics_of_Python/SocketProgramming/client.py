import socket


try:
    c = socket.socket()

    c.connect(('localhost',9001))
    print(c.recv(1024).decode())   # 1024 is the buffer for receiving the data from the server as this is a client
    clientName = input("Enter Your name: ")
    c.send(bytes(clientName, "utf-8"))
except Exception as e:
    print("Connection error", e)