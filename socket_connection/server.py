import socket

# Create a socket object (IPv4, TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name and bind to a port
host = '127.0.0.1'  # localhost
port = 9999
server_socket.bind((host, port))

# Start listening for incoming connections
server_socket.listen(1)
print(f"[+] Server listening on {host}:{port}")

try:
    client_socket, address = server_socket.accept()
    print(f"[+] Connected to {address}")

    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"[Client]: {data}")
        response = f"Received: {data}"
        client_socket.send(response.encode())

except Exception as e:
    print(f"[!] Error: {e}")
finally:
    client_socket.close()
    server_socket.close()
    print("[*] Server closed connection")