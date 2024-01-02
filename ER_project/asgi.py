"""
ASGI config for ER_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from ERapp.routing import websocket_urlpatterns
#from channels.middleware.websocket import WebSocketMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ER_project.settings')

#applicationsd = get_asgi_application()

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(websocket_urlpatterns),  
})

