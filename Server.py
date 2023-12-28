import socket

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Client {address} connected")

        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            
            print(f"Received message from {address}: {data}")
            broadcast_message(client_socket, address, data)
        
        print(f"Client {address} disconnected")
        client_socket.close()

def broadcast_message(sender_socket, sender_address, message):
    for client_socket, client_address in clients:
        if client_socket != sender_socket:
            try:
                client_socket.sendall(message.encode())
            except socket.error:
                # Обработка ошибок, если отправка сообщения не удалась
                pass

clients = []

host = "127.0.0.1"
port = 12345
start_server(host, port)