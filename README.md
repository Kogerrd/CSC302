

import socket

# Define server address and port
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Port to listen on

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to the address and port
server_socket.bind((HOST, PORT))

# Listen for connections
server_socket.listen(5)
print(f"Server listening on {HOST}:{PORT}...")

while True:
    # Accept a connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    # Send a response to the client
    message = "Hello, Client! You are connected to the server."
    client_socket.send(message.encode())

    # Close the connection
    client_socket.close()

    
