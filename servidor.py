import socket
import threading
def handle_client(client_socket):
    while True:
        # Recibir datos del cliente
        data = client_socket.recv(1024)
        if not data:
            break
