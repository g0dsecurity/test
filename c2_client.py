import socket

# Define the C2 server's IP address and port
SERVER_IP = '192.168.1.6'
SERVER_PORT = 4444

def connect_to_server():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the C2 server
        client_socket.connect((SERVER_IP, SERVER_PORT))

        # Send a message to the server
        message = 'Hello, C2 server!'
        client_socket.sendall(message.encode())

        # Receive data from the server
        response = client_socket.recv(1024).decode()
        print(f'Received from server: {response}')

    except Exception as e:
        print(f'Error: {e}')

    finally:
        # Close the socket connection
        client_socket.close()

if __name__ == '__main__':
    connect_to_server()