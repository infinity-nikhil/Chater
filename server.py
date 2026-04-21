import asyncio
from websockets.asyncio.server import serve

clients = {}  # username -> websocket

async def handler(websocket):
    await websocket.send("Enter your name:")
    name = await websocket.recv()

    clients[name] = websocket
    print(f"{name} connected")

    try:
        async for message in websocket:

            # 👉 check DM format
            if message.startswith("@"):
                try:
                    target_name, msg = message.split(" ", 1)
                    target_name = target_name[1:]  # remove @

                    if target_name in clients:
                        target_ws = clients[target_name]

                        # send to receiver
                        await target_ws.send(f"{name} (DM): {msg}")

                        # optional: sender ko bhi dikhao
                        await websocket.send(f"You → {target_name}: {msg}")

                    else:
                        await websocket.send("User not found ❌")

                except:
                    await websocket.send("Invalid format. Use: @username message")

            else:
                # fallback: broadcast (optional)
                for user, ws in clients.items():
                    if ws != websocket:
                        await ws.send(f"{name}: {message}")

    except:
        pass

    finally:
        del clients[name]
        print(f"{name} disconnected")

async def main():
    async with serve(handler, "localhost", 8765):
        print("Server running...")
        await asyncio.Future()

asyncio.run(main())