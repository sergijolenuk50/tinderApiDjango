# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def chat_view(request, user_id):
    # Логіка для обробки чату, наприклад:
    return render(request, 'chat/chat_view.html', {'user_id': user_id})


# chat/views.py
# from django.shortcuts import render
# from .models import User
# from django.http import Http404

# def chat_view(request, user_id):
#     try:
#         user = User.objects.get(id=user_id)
#     except User.DoesNotExist:
#         raise Http404("User not found")
    
#     # Якщо користувач знайдений, передаємо його в шаблон
#     return render(request, 'chat/chat_view.html', {'user': user})