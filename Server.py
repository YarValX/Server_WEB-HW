import socket
import threading

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    clients = []  # Список клиентских сокетов и адресов

    def handle_client(client_socket, address):
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            
            print(f"Received message from {address}: {data}")
            broadcast_message(client_socket, data)
        
        print(f"Client {address} disconnected")
        client_socket.close()
        clients.remove((client_socket, address))

    def broadcast_message(sender_socket, message):
        for client_socket, client_address in clients:
            if client_socket != sender_socket:
                try:
                    client_socket.sendall(message.encode())
                except socket.error:
                    # Обработка ошибок, если отправка сообщения не удалась
                    pass

    while True:
        client_socket, address = server_socket.accept()
        print(f"Client {address} connected")
        
        clients.append((client_socket, address))

        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()

start_server("127.0.0.1", 12345)