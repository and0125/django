from django.urls import re_path # relative path method
from .consumers import ChatRoomConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatRoomConsumer),
]
