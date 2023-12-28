import socket

def start_server():
    # Создание сокета
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind сокета на локальный адрес и порт
    server_address = ('localhost', 5000)
    server_socket.bind(server_address)

    # Включение режима прослушивания на входящие соединения
    server_socket.listen(1)

    print('Сервер запущен. Ожидание клиента...')

    while True:
        # Принятие входящего соединения
        client_socket, client_address = server_socket.accept()

        # Обработка данных от клиента
        data = client_socket.recv(1024).decode()
        print('Получен запрос от клиента:', data)

        # Отправка ответа клиенту
        response = 'Привет, клиент!'
        client_socket.sendall(response.encode())

        # Закрытие соединения
        client_socket.close()