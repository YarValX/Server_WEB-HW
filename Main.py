import multiprocessing
import Server
import Client

if __name__ == '__main__':
    # Запуск сервера в отдельном процессе
    server_process = multiprocessing.Process(target=Server.start_server)
    server_process.start()

    # Запуск клиента в отдельном процессе
    client_process = multiprocessing.Process(target=Client.send_request)
    client_process.start()

    # Ожидание завершения работы сервера и клиента
    server_process.join()
    client_process.join()