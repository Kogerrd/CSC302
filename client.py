import socket

# Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_host = '127.0.0.1'  # Localhost
server_port = 12345

try:
    # Connect to the server
    client_socket.connect((server_host, server_port))
    print(f"Connected to server at {server_host}:{server_port}")

    # Send a message to the server
    message = "Hello, Server!"
    client_socket.send(message.encode())

    # Receive and print the response from the server
    response = client_socket.recv(1024).decode()
    print(f"Server: {response}")

except ConnectionRefusedError:
    print("Connection failed. Ensure the server is running.")

finally:
    # Close the socket
    client_socket.close()
