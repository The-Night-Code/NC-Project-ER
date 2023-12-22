# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from .models import UserStatus
import logging

class UserStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.update_user_status(True)

    async def disconnect(self, close_code):
        await self.update_user_status(False)

    async def update_user_status(self, is_online):
        user_status, created = UserStatus.objects.get_or_create(user=self.scope['user'])
        user_status.is_online = is_online
        user_status.save()

        # Broadcast the updated user status to all connected clients
        await self.send_user_status()

    async def send_user_status(self):
        online_users = UserStatus.objects.filter(is_online=True).values_list('user__username', flat=True)
        offline_users = UserStatus.objects.filter(is_online=False).values_list('user__username', flat=True)

        # Broadcast the online and offline user lists to all clients
        await self.send(text_data=json.dumps({
            'type': 'user_status',
            'online_users': list(online_users),
            'offline_users': list(offline_users),
        }))


class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Perform connection setup if needed
        await self.accept()

    async def disconnect(self, close_code):
        # Perform cleanup on disconnect
        pass

    async def receive(self, text_data):
        # Process received data
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message')

        # Do something with the received data (e.g., print to console)
        print(f"Received message from client: {message}")

        # Optionally, send a response back to the client
        response_message = "Message received successfully!"
        await self.send(text_data=json.dumps({'response': response_message}))
        
    

    

class ChatConsumer234(AsyncWebsocketConsumer):
    async def connect(self):
        # Extract user ID from the URL or any other source (e.g., token)
        user_ = self.scope.get('user')

        # Create a unique group name for each user
        self.roomGroupName = "group_chat_gfg" # f"{user_.id}"

        # Add the user to the group
        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )

        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Remove the user from the group when the WebSocket is closed
        await self.channel_layer.group_discard(
            self.roomGroupName,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send the received message to the group (all connected clients of the same user)
        await self.channel_layer.group_send(
            self.roomGroupName,
            {
                'type': 'chat.message',
                'message': message
            }
        )

    async def chat_message(self, event):
        # Send the message to the WebSocket
        await self.send(text_data=json.dumps({'message': event['message']}))
        
        
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.roomGroupName = "group_chat_gfg"
        await self.channel_layer.group_add(
            self.roomGroupName ,
            self.channel_name
        )
        await self.accept()
    async def disconnect(self , close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName , 
            self.channel_layer 
        )
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        email = text_data_json["email"]
        
        box = text_data_json["box"]
        cellId = text_data_json["cellId"]
        
        
        await self.channel_layer.group_send(
            self.roomGroupName,{
                "type" : "sendMessage" ,
                "message" : message , 
                "email" : email ,
                "box":box ,
                "cellId":cellId,
            })
    async def sendMessage(self , event) : 
        user_ = self.scope.get('user')
        message = event["message"]
        email = event["email"]
        box = event["box"]
        cellId = event["cellId"]
        await self.send(text_data = json.dumps({"message":message ,
                                                "email":email,
                                                "box":box ,
                                                "cellId":cellId}))