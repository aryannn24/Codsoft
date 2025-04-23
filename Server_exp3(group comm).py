import socket
import threading

# Store all client connections
clients = []

def handle_client(client_socket, address):
    print(f"[+] New connection from {address}")


    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"[{address}] says: {message}")
            broadcast(f"[{address}] says: {message}", client_socket)
        except:
            break

    print(f"[-] Disconnected from {address}")
    clients.remove(client_socket)
    client_socket.close()

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                clients.remove(client)

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen()

    print("[*] Server started. Waiting for clients...")

    while True:
        client_socket, address = server.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()

if __name__ == "__main__":
    main()
