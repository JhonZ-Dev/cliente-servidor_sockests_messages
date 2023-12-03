import socket

def start_client():
    # Configurar el cliente
    host = '127.0.0.1'
    port = 12345
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    while True:
        # Enviar un mensaje al servidor
        message = input("Ingrese un mensaje para el servidor (o 'exit' para salir): ")
        if message.lower() == 'exit':
            break
