import asyncio
import json
import logging
import websockets
from abc import ABC, abstractmethod

class Connection(ABC):
    def run(self):
        start_server = websockets.serve(self.connect, "localhost", 3030)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

    async def connect(self, websocket, path):
        try:
            async for message in websocket:
                incomingJson = json.loads(message)
                await self.analyze(incomingJson,websocket)
        except:
            pass
        finally:
            disconnectJson = {'type': 'disconnect'}# tworzenie jsona że ktos sie zerwal i wyslanie go do analyze - command factory
            await self.analyze(disconnectJson, websocket)

    async def analyze(self,data,websocket):
        pass #abstract