import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        self.other_user = User.objects.get(id=self.user_id)
        self.room_name = f"chat_{self.scope['user'].id}_{self.user_id}"
        self.room_group_name = f"chat_{self.room_name}"

        # Приєднатися до кімнати WebSocket
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Підтвердити підключення
        await self.accept()

    async def disconnect(self, close_code):
        # Вийти з кімнати при закритті з'єднання
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Отримувати повідомлення від WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_content = text_data_json['message']

        # Зберігати повідомлення в базі даних
        message = Message.objects.create(
            sender=self.scope['user'],
            receiver=self.other_user,
            content=message_content
        )

        # Відправити повідомлення в кімнату
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message_content,
                'sender': self.scope['user'].username
            }
        )

    # Отримувати повідомлення з групи
    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        # Відправити повідомлення WebSocket клієнту
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))
