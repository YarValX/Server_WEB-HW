import socket
import threading

def handle_client(client_socket, client_address):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                print(f"Received message from {client_address}: {message}")
                # Отправка сообщения клиентам, кроме отправителя
                broadcast(message, client_socket)
            else:
                remove_client(client_socket)
                print(f"Client {client_address} disconnected")
                break
        except Exception as e:
            print(f"An error occurred for client {client_address}: {str(e)}")
            remove_client(client_socket)
            break

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            client.send(message.encode("utf-8"))

def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

HOST = '127.0.0.1'
PORT = 12345

clients = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Server listening on {HOST}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    print(f"Client {client_address} connected")
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()