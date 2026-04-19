import asyncio
from websockets.asyncio.server import serve

clients = {}  # websocket -> username

async def handler(websocket):
    # 👤 Step 1: username 
    await websocket.send("Enter your name:")
    name = await websocket.recv()

    # store user
    clients[websocket] = name
    print(f"{name} connected")

    # 🔔 notify others
    for client in clients:
        if client != websocket:
            await client.send(f"{name} joined the chat")

    try:
        async for message in websocket:
            # 📨 send to everyone with name
            for client in clients:
                if client != websocket:
                    await client.send(f"{name}: {message}")

    except:
        pass

    finally:
        # ❌ remove on disconnect
        left_user = clients[websocket]
        del clients[websocket]

        for client in clients:
            await client.send(f"{left_user} left the chat")

        print(f"{left_user} disconnected")

async def main():
    async with serve(handler, "localhost", 8765):
        print("Server running...")
        await asyncio.Future()

asyncio.run(main())