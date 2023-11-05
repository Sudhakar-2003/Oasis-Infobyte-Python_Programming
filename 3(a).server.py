import socket
import threading

# Server Configuration
host = "192.168.43.182"  # Use your host IP or "127.0.0.1" for localhost
port = 12345

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen()

# List to store connected clients
clients = []

# Function to broadcast messages to all clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode())
            except:
                # Remove the client if there is an issue
                clients.remove(client)

# Function to handle client connections
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                # Remove the client if they disconnect
                clients.remove(client_socket)
                client_socket.close()
                break
            broadcast(message, client_socket)
        except:
            pass

# Accept and handle incoming connections
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connected with {str(client_address)}")

    # Add the new client to the list
    clients.append(client_socket)

    # Start a new thread to handle the client
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()
