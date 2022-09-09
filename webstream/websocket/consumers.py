from channels.consumer import AsyncConsumer

class LiveChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept"
        })
        print("connect", event)

    async def websocket_receive(self, event):
       print("receive", event)

    async def websocket_error(self, event):
        print("error", event)

    async def websocket_disconnect(self, event):
        print("disconnect", event)