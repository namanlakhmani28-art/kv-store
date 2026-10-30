import socket
import threading


# Our in-memory data store (RAM)
store = {}




def handle_client(client_socket):
    """Handles an individual client connection."""

    try:
        while True:
            data = client_socket.recv(1024).decode('utf-8').strip()

            if not data:
                break

            parts = data.split(" ", 2)
            command = parts[0].upper()

            if command == "SET" and len(parts) == 3:
                key, value = parts[1], parts[2]
                store[key] = value
                client_socket.sendall(b"OK\n")

            elif command == "GET" and len(parts) == 2:
                key = parts[1]
                value = store.get(key, "(nil)")
                client_socket.sendall(f"{value}\n".encode('utf-8'))


            else:
                client_socket.sendall(b"ERR unknown command or syntax\n")


        
    finally:
        client_socket.close()

    

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind(('127.0.0.1', 6379))

    server.listen()

    print("Concurrent KV Store listening on port 6379...")

    while True:
        client, address = server.accept()

        print(f"Connected by {address}")


        #Spin up  a new thread for each client so multiple can connect
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()



if __name__ == "__main__":
    start_server()