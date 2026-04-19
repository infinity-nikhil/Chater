from websockets.sync.client import connect

#Adding a while loop to send messsage through terminal 

def chat():
    with connect("ws://localhost:8765") as websocket:
        print("Welcome to Chater. Type 'exit' to quit.\n")

        while True:
            msg = input("Alice: ")

            if msg.lower() == "exit": 
                print("Connection closed")
                break
            
            websocket.send(msg)
            reply = websocket.recv()
            print(f"Received: {reply}")  

chat()

