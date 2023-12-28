import socket
import threading

def start_server():
    # Создание сокета
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind сокета на локальный адрес и порт
    server_address = ('localhost', 5000)
    server_socket.bind(server_address)

    # Включение режима прослушивания на входящие соединения
    server_socket.listen(1)

    print('Сервер запущен. Ожидание клиента...')

    # Список подключенных клиентов
    clients = []

    def handle_client(client_socket, client_address):
        while True:
            try:
                # Обработка данных от клиента
                data = client_socket.recv(1024).decode()
                print(f'Получен запрос от клиента {client_address}: {data}')

                # Отправка запроса всем остальным клиентам
                for client in clients:
                    if client != client_socket:
                        client.sendall(data.encode())

            except ConnectionResetError:
                print(f'Клиент {client_address} отключился')
                clients.remove(client_socket)
                client_socket.close()
                break

    while True:
        # Принятие входящего соединения
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        print(f'Клиент подключился: {client_address}')

        # Создание и запуск отдельного потока для обработки клиента
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()