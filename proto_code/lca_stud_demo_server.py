#!/usr/bin/env python


import asyncio
import json
import logging
import websockets


logging.basicConfig()


USERS = set()


NODES = None


def users_event():
    return json.dumps({"type": "users", "count": len(USERS)})


def change_event():
    return json.dumps({"type": "change"})


async def counter(websocket):
    global USERS, NODES
    try:
        # Register user
        USERS.add(websocket)
        # websockets.broadcast(USERS, users_event())
        await websocket.send(change_event())
        # Manage state changes
        async for message in websocket:
            if json.loads(message) != NODES:
                NODES = json.loads(message)
                OTHER_USERS = USERS.copy()
                OTHER_USERS.remove(websocket)
                websockets.broadcast(OTHER_USERS, json.dumps(NODES))
    finally:
        # Unregister user
        USERS.remove(websocket)
        # websockets.broadcast(USERS, users_event())


async def main():
    async with websockets.serve(counter, "localhost", 6789):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
