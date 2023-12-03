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
