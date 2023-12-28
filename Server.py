import socket
import threading

def handle_client(client_socket, client_address):
    while True:
        data = client_socket.recv(1024).decode()
        if "quit" in data:
            break
        broadcast(data)
    client_socket.close()

def broadcast(message):
    for client_socket in clients:
        client_socket.send(message.encode())

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 1234))
server_socket.listen(5)

clients = []

print("Сервер запущен.")

while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    print(f"Подключился клиент {client_address[0]}:{client_address[1]}")
    threading.Thread(target=handle_client, args=(client_socket, client_address)).start()