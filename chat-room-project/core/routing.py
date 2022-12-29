"""
This module sets up the router to send data to the Websocket server.

This module works similarly to the urls.py file, it contains the routes for accessing the chatroom Websockets.

The AuthMiddlewareStack forces users to login and can be used more extensively than in this example. Here, this is used for identifying the user that's logged in to use their username in the channel.

Eventually, this module will be connected to a routing file in the Chat Django App.

"""
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

# this determines how Websocket protocol requests will be mapped
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})