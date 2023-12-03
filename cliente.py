import socket

def start_client():
    # Configurar el cliente
    host = '127.0.0.1'
    port = 12345
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))