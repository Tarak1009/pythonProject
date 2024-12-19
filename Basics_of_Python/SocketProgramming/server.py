import socket

try:
    s = socket.socket()
    s.bind(("localhost", 9001))
    s.listen(3)             # listen 3 means it will listen to only 3 connections and if any 4th connection is made then it will reject it.
    print("waiting for connections")

    while True:
        c, addr = s.accept()
        c.send(bytes("Welcome to Server", "utf-8"))     # Remember to send the data in the bytes format with utf-8 encoding
        name = c.recv(1024).decode()            # 1024 is the buffer for receiving the data from the client as this is a server
        print("Connected successfully ", addr, name)
        c.close()

except Exception as e:
    print("Connection error: ", e)