import socket
import threading

# Client Configuration
host = "192.168.43.182"  # Use the same host and port as the server
port = 12345

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# Function to send messages
def send_message():
    while True:
        message = input()
        client_socket.send(message.encode())

# Function to receive messages
def receive_message():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            # Handle any exceptions
            print("Connection lost.")
            client_socket.close()
            break

# Start separate threads for sending and receiving messages
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)

send_thread.start()
receive_thread.start()


