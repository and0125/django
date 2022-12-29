from channels.generic.websocket import AsyncWebSocketConsumer
import json


class ChatRoomConsumer(AsyncWebSocketConsumer):
    # this is an asynchronous function in python. Calling an async function immediately starts a co-routine, and "awaits" the what is specified before returning any data.
    async def connect(self):
        # grabs the roomname from the request
        self.room_name = self.scope["url_route"]['kwargs']['room_name']
        # this is defining the user group name
        self.room_group_name = 'chat_%s' % self.room_name
        
        
        # This creates a new group with the input room name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'test message',
                'tester': 'hello world',
            }
        )

    async def tester_message(self, event):
        tester = event['tester']

        await self.send(text_data= json.dumps({'tester': tester}))

    async def disconnect(self, close_code):
        # This method will discard the group

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

