import socket

try:
    s = socket.socket()

    s.bind(("localhost", 9001))


    s.listen(3)
    print("waiting for connections")

    while True:
        c, addr = s.accept()
        c.send(bytes("Welcome to Server", "utf-8"))
        name = c.recv(1024).decode()
        print("Connected successfully ", addr, name)
        c.close()

except Exception as e:
    print("Connection error: ", e)

