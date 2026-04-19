from websockets.sync.client import connect
import threading

def receive_messages(ws): 
    while True:
        try: 
            message = ws.recv()
            print(f"{message}")
        except:
            break

def chat():
    with connect("ws://localhost:8765") as websocket:
        print("Welcome to Chater. Type 'exit' to quit.\n")
        # first message = name
        name_prompt = websocket.recv()
        name = input(name_prompt + " ")
        websocket.send(name)


        # start background listener
        threading.Thread(target=receive_messages, args=(websocket,), daemon=True).start()

        while True:
            msg = input("")

            if msg.lower() == "exit": 
                print("Connection closed")
                break
            
            websocket.send(msg) 

chat()
