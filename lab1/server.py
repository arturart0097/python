import socket
import threading

# Створення сокету для TCP-сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Задання IP-адреси та порту сервера
host = '127.0.0.1'
port = 12345

# Прив'язка серверного сокету до IP-адреси та порту
server_socket.bind((host, port))

# Сервер слухає на вказаному порту
server_socket.listen(5)

print(f"Сервер слухає на {host}:{port}")

# Список для зберігання з'єднань клієнтів
client_connections = []

# Функція для обробки повідомлень від клієнта
def handle_client(client_socket, client_address):
    while True:
        try:
            # Отримання даних від клієнта
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break

            # Виведення отриманого повідомлення
            print(f"Від {client_address[0]}:{client_address[1]}: {data}")

            # Пересилання повідомлення всім іншим клієнтам
            for connection in client_connections:
                if connection != client_socket:
                    connection.send(data.encode('utf-8'))
        except:
            break

    # Видалення з'єднання зі списку
    client_connections.remove(client_socket)
    client_socket.close()

# Приймання та обробка підключень від клієнтів
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Підключено клієнта {client_address[0]}:{client_address[1]}")

    # Додавання з'єднання до списку
    client_connections.append(client_socket)

    # Створення окремого потоку для обробки клієнта
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
