from websockets.sync.client import connect
import threading

#Now have to modify cause: websocket.recv() gets only called when we send something
# We don't want to happen that right? We want ki it recive all the time ...not only when we send something

def receive_messages(ws): 
    while True:
        try: 
            message = ws.recv()
            print(f"\nServer: {message}")
        except:
            break

def chat():
    with connect("ws://localhost:8765") as websocket:
        print("Welcome to Chater. Type 'exit' to quit.\n")

        # start background listener
        threading.Thread(target=receive_messages, args=(websocket,), daemon=True).start()

        while True:
            msg = input("Alice: ")

            if msg.lower() == "exit": 
                print("Connection closed")
                break
            
            websocket.send(msg) 

chat()

#Seperated the send and the recv function  
# How to use it ?
# Just open client.py in multiple terminals 
