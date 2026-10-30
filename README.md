# Multi-Threaded In-Memory Key-Value Store

A lightweight, concurrent, in-memory key-value database engine built from scratch in Python. It supports real-time network communication over TCP sockets, thread-safe access across concurrent clients, and maintains $O(1)$ average time complexity for core operations.

---

## 🚀 Features

- **Concurrent Client Support:** Utilizes multithreading to manage multiple simultaneous client connections without blocking.
- **Thread-Safe Data Operations:** Employs explicit synchronization primitives (locks) to safely execute concurrent mutations and prevent data races.
- **$O(1)$ Time Complexity:** Leverages optimized hash table mechanics to deliver $O(1)$ average-case performance for `SET`, `GET`, and `DELETE` operations.
- **TCP Socket Server:** Custom networking layer built using Python's `socket` library to handle command transmission over local network protocols.

---

## 🛠️ Architecture Overview

```
[ Client 1 ] \
[ Client 2 ] -- TCP Connections --> [ Socket Server ] --> [ Thread Manager ] --> [ Mutex Lock ] --> [ Memory Store ]
[ Client 3 ] /
```

1. **Server Initialization:** Binds to a local host and port, listening for incoming TCP streams.
2. **Connection Handler:** Spawns a dedicated thread for every new client connection.
3. **Synchronization Layer:** Ensures that write and delete actions acquire mutual exclusion locks before modifying internal data structures.

---

## 📂 Project Structure

```text
kv-store/
├── server.py       # Main socket server & multithreading logic
├── client.py       # Terminal client for sending commands
├── .gitignore      # Git exclusion rules
└── README.md       # Project documentation
```

---

## 🚦 Getting Started

### Prerequisites

- Python 3.8+ installed on your system.

### Running the Project

1. **Clone the repository:**
   ```bash
   git clone https://github.com/namanlakhmani28-art/kv-store.git
   cd kv-store
   ```

2. **Start the Key-Value Server:**
   ```bash
   python3 server.py
   ```

3. **In a new terminal window, start a Client connection:**
   ```bash
   python3 client.py
   ```

---

## 💻 Supported Commands

| Command | Usage | Description | Example |
| :--- | :--- | :--- | :--- |
| **`SET`** | `SET <key> <value>` | Inserts or updates a key-value pair | `SET user1 Naman` |
| **`GET`** | `GET <key>` | Retrieves the value associated with `<key>` | `GET user1` |
| **`DELETE`** | `DELETE <key>` | Removes the specified key-value pair | `DELETE user1` |

---

## 🧪 Future Improvements

- [ ] Add persistent snapshotting to disk (AOF / RDB logging).
- [ ] Implement key eviction policies (LRU / TTL handling).
- [ ] Add benchmarking tools to measure maximum queries per second (QPS).

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for details.
