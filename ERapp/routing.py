from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path,re_path
from .consumers import ChatConsumer,MyConsumer
from . import consumers

#applicationvbn = ProtocolTypeRouter({
#    'websocket': AuthMiddlewareStack(
#        URLRouter(
#            [
#                path("ws/chat/", ChatConsumer.as_asgi()),
#            ]
#        )
#    ),
#})

websocket_urlpatterns = [
    re_path(r'ws/user_status/$', consumers.UserStatusConsumer.as_asgi()),
    #re_path(r'ws/chat/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/chat/$', ChatConsumer.as_asgi()),
    #re_path("" , ChatConsumer.as_asgi()) , 

    # Add more WebSocket routes if needed
]

