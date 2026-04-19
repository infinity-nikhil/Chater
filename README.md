# 🚀 Python WebSocket: Basic Client-Server Setup

A minimal implementation of a **bidirectional WebSocket connection** in Python using the `websockets` library.

This project demonstrates how a client and server can communicate in real-time without the traditional HTTP request-response cycle.

---

## 📌 Features

* 🔁 Real-time bidirectional communication
* ⚡ Async WebSocket server using `asyncio`
* 💬 Simple echo server implementation
* 🧪 Beginner-friendly code structure

---

## 🧠 How It Works

* The **server** listens for incoming WebSocket connections.
* The **client** connects to the server and sends a message.
* The server receives the message and sends it back (echo).
* The client receives and prints the response.

---

## 📂 Project Structure

```
.
├── server.py   # WebSocket server (async)
├── client.py   # WebSocket client (sync)
└── README.md
```

---

## ⚙️ Requirements

* Python 3.10+
* websockets library

Install dependencies:

```bash
pip install websockets
```

---

## ▶️ Running the Project

### 1. Start the Server

```bash
python server.py
```

---

### 2. Run the Client

```bash
python client.py
```

---

## 🧪 Code Overview

### Server (`server.py`)

* Uses `asyncio` for handling multiple connections
* Listens on `ws://localhost:8765`
* Echoes back any message received

### Client (`client.py`)

* Connects to the WebSocket server
* Sends a message
* Waits and prints the response

---

## 🤝 Contributing

This is a personal learning project, but suggestions and improvements are welcome.

---

## 📄 License

MIT License
