import asyncio
from websockets.asyncio.server import serve

#Now the upgrade shall be ki we make two clients and send the message each other

connected_clients = set() # an empty set, will store all the connected clients 

async def handler(websocket):  #See if any one connected via websocket 
    #  new client connected
    connected_clients.add(websocket) #The one connected gets added into connected_client
    print("New client connected", websocket)

    try:
        async for message in websocket:   #And then same old step 
            print(f"Received: {message}")

            #  broadcast to ALL clients
            for client in connected_clients:   #for loop over the data of connected_clients 
                if client != websocket:  # (optional: skip sender)
                    await client.send(message)

    except:
        print("Client disconnected")

    finally:
        #  remove client when it leaves
        connected_clients.remove(websocket)

async def main(): #And then same old step 
    async with serve(handler, "localhost", 8765):
        print("Server started...")
        await asyncio.Future()  # run forever

asyncio.run(main())