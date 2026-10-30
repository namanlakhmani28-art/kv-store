import socket
import concurrent.futures

def send_request(key, value):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 6379))
        # Send a SET command
        s.sendall(f"SET {key} {value}\n".encode('utf-8'))
        print(s.recv(1024).decode('utf-8').strip())

# Simulate 5 clients writing at the exact same time
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    for i in range(1000):
        executor.submit(send_request, f"user_{i}", f"score_{i*10}")