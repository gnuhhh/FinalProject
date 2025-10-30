from channels.generic.websocket import WebsocketConsumer
from .models import *
from django.shortcuts import get_object_or_404  
from django.template.loader import render_to_string
from asgiref.sync import async_to_sync 
import json     
class ChatroomConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope["user"]
        self.chatroom_name = self.scope['url_route']['kwargs']['chatroom_name'] 
        self.chatroom = get_object_or_404(ChatGroup, group_name=self.chatroom_name)
        async_to_sync(self.channel_layer.group_add)(
            self.chatroom_name, self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.chatroom_name, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        chat_message = GroupMessage.objects.create(message=message, sender=self.user, group=self.chatroom)
        event = {
            'type': 'message_handler',
            'chat_message_id': chat_message.id,
        }
        async_to_sync(self.channel_layer.group_send)(
            self.chatroom_name, event
        )

    def message_handler(self, event):
        chat_message_id = event['chat_message_id']
        chat_message = GroupMessage.objects.get(id=chat_message_id)
        html = render_to_string('chat/partials/chat_message_p.html', {'message': chat_message, 'user': self.user})
        self.send(text_data=html)