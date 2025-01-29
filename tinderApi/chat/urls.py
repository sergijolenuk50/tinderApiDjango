from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/', views.chat_view, name='chat_view'),
]

# from django.urls import path
# from . import consumers

# websocket_urlpatterns = [
#     path('ws/chat/<int:user_id>/', consumers.ChatConsumer.as_asgi()),
# ]