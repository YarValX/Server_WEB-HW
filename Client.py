import socket

def send_request():
    # Создание сокета
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Подключение к серверу
    server_address = ('localhost', 5000)
    client_socket.connect(server_address)

    # Отправка запроса серверу
    request = 'Привет, сервер!'
    client_socket.sendall(request.encode())

    # Получение ответа от сервера
    response = client_socket.recv(1024).decode()
    print('Получен ответ от сервера:', response)

    # Закрытие соединения
    client_socket.close()