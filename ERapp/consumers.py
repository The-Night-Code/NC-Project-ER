# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import USER,UserStatus,message_box_1
import logging

import random
import string


def generate_random_string(length):
    characters = string.ascii_letters + string.digits  # You can customize this for your needs
    random_string = ''.join(random.choice(characters) for _ in range(length))
    random_string=random_string.replace("%20","")
    random_string=random_string.replace(" ","")
    return random_string

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
        
    

    
@database_sync_to_async
def get_user_object(email):
    return USER.objects.get(email=email)

@database_sync_to_async
def create_new_message(msg_id, cell_id, username, email, message_text, col, user_profile_pic):
    return message_box_1.objects.create(
        message_id=msg_id,
        row_id=cell_id,
        username=username,
        email=email,
        message=message_text,
        box=col,
        profile_pic=user_profile_pic
    )

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.roomGroupName = "chat_rooms"
        await self.channel_layer.group_add(
            self.roomGroupName ,
            self.channel_name
        )
        await self.accept()
    async def disconnect(self , close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName , 
            self.channel_name #self.channel_name channel_layer
        )
    async def receive(self, text_data):
        user_ = self.scope.get('user')

        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        email = text_data_json["email"]
        username = text_data_json["username"]
        userProfilePic = text_data_json["userProfilePic"]
        col = text_data_json["col"]
        cellId = text_data_json["cellId"]
        
        obj_user = await get_user_object(email)
        user_profile_pic = getattr(obj_user, "profile_pic")

        if message:
            msg_id = generate_random_string(10)

            # Use database_sync_to_async to execute the create operation asynchronously
            await create_new_message(msg_id, cellId, username, email, message, col, user_profile_pic)
                
        
            await self.channel_layer.group_send(
                self.roomGroupName,{
                    "type" : "sendMessage" ,
                    "email":email,
                    "username":username ,
                    "userProfilePic":userProfilePic,
                    "message":message ,
                    "col":col ,
                    "cellId":cellId
                })
        
        
    async def sendMessage(self , event) : 
        user_ = self.scope.get('user')
        email = event["email"]
        username = event["username"]
        userProfilePic = event["userProfilePic"]
        message = event["message"]
        col = event["col"]
        cellId = event["cellId"]

        obj_user = await get_user_object(email)
        user_profile_pic = getattr(obj_user, "profile_pic")
        if message:
            await self.send(text_data = json.dumps({
                                                    "email":email,
                                                    "username":username ,
                                                    "userProfilePic":userProfilePic,
                                                    "message":message ,
                                                    "col":col ,
                                                    "cellId":cellId}))