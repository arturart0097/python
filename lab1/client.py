import socket

# Створення сокету для TCP-клієнта
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Задання IP-адреси та порту сервера, до якого потрібно підключитися
server_host = '127.0.0.1'
server_port = 12345

# Підключення до сервера
client_socket.connect((server_host, server_port))

while True:
    # Введення тексту користувачем
    message = input("Введіть текст для відправки на сервер (або 'завершити' для завершення): ")

    # Відправлення даних на сервер
    client_socket.send(message.encode('utf-8'))

    # Перевірка, чи користувач бажає завершити з'єднання
    if message == "завершити":
        break

# Закриття з'єднання з сервером
client_socket.close()
