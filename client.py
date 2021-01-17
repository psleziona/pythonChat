import socket, threading

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def recive(conn):
    while True:
        data = conn.recv(1024)
        if len(data) > 1:
            print(data.decode())


socket.connect(('127.0.0.1', 5001))
print(socket.recv(1024))
name = input()
socket.send(name.encode())
print(socket.recv(1024).decode('utf-8'))

r = threading.Thread(target=recive, args=(socket,))
r.daemon = True
r.start()

while True:
    msg = input('')
    socket.send(msg.encode())
    
socket.close()