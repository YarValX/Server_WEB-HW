import socket

def send_request():
    # Создание сокета
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Подключение к серверу
    server_address = ('localhost', 5000)
    client_socket.connect(server_address)

    # Цикл обмена сообщениями
    while True:
        # Отправка запроса серверу
        request = input('Введите сообщение: ')
        client_socket.sendall(request.encode())

        # Получение ответа от сервера
        response = client_socket.recv(1024).decode()
        print('Получен ответ от сервера:', response)

        # Если пользователь ввел "exit", то выход из цикла и закрытие соединения
        if request == 'exit':
            break

    # Закрытие соединения
    client_socket.close()