import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server details
host = '127.0.0.1'  # localhost
port = 9999

try:
    client_socket.connect((host, port))
    print(f"[+] Connected to server at {host}:{port}")

    # Send message to server
    message = "Hello Server!"
    client_socket.send(message.encode())

    # Receive and print response
    response = client_socket.recv(1024).decode()
    print(f"[Server]: {response}")

except Exception as e:
    print(f"[!] Connection failed: {e}")
finally:
    client_socket.close()
    print("[*] Disconnected from server")