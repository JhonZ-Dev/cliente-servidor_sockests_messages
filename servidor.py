import socket
import threading
def handle_client(client_socket):
    while True:
        # Recibir datos del cliente
        data = client_socket.recv(1024)
        if not data:
            break
        # Imprimir los datos recibidos
        print(f"Mensaje recibido del cliente: {data.decode('utf-8')}")

        # Responder al cliente
        response = "Mensaje recibido correctamente"
        client_socket.send(response.encode('utf-8'))
    # Cerrar la conexión con el cliente
    client_socket.close()


def start_server():
    # Configurar el servidor
    host = '127.0.0.1'
    port = 12345
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Servidor
          escuchando en {host}:{port}")
    while True:
        # Esperar a que un cliente se conecte
        client_socket, addr = server.accept()
        print(f"Cliente conectado desde {addr[0]}:{addr[1]}")
# Iniciar un hilo para manejar al cliente
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()
if __name__ == "__main__":
    start_server()