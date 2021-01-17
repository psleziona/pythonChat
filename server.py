import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 5001))

server.listen(10)

def handle_con(conn):
	while True:
		msg = conn.recv(1024).decode()
		user = users.get(conn)['name']
		if msg == '/exit':
			server.send(bytearray(f'{user} left', 'utf-8'))
			conn.close()
			break
		print(f'<{user}>: {msg}')
		send_to_all(conn, msg)


def on_new_connection(conn):
	conn.send(bytearray('Enter name', 'utf-8'))
	name = conn.recv(1024).decode('utf-8')
	conn.send(bytearray(f'Hello {name}', 'utf-8'))
	users[conn] = {
		'name': name
	}
	user = threading.Thread(target=handle_con, args=(conn,))
	user.daemon = True
	user.start()


def send_to_all(conn, msg):
	sender = users.get(conn)['name']
	for connected_user in users.keys():
		if connected_user != conn:
			connected_user.send(bytearray(f'<{sender}>: {msg}', 'utf-8'))

users = {}

while True:
	conn, addr = server.accept()
	print(f'{addr[0]}:{addr[1]} connected!')
	on_new_connection(conn)


server.close()