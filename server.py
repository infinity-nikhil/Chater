import asyncio
from websockets.asyncio.server import serve

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)
        print(message);

async def main():
    print("Server is on BIATCH")
    async with serve(echo, "localhost", 8765) as server:
        await server.serve_forever()

asyncio.run(main())