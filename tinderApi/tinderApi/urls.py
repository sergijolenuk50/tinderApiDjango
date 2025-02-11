"""
URL configuration for tinderApi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
    #django_auth/urls.py
from django.contrib import admin
from django.urls import path, include
from users.views import UserCreateView
# from .views import UserCreateView, MyTokenObtainPairView, MyTokenRefreshView  
from users.views import MyTokenObtainPairView, MyTokenRefreshView  
# from chat import views
# from django.urls import path
# from . import views

app_name = 'chat'

urlpatterns = [
path('admin/', admin.site.urls),
# path('accounts/', include('django.contrib.auth.urls')),
path('register/', UserCreateView.as_view(), name='register'),
# path('api/users/', UserCreateView.as_view(), name='user-create'),  
path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),  
#path('api/token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),  
# path('<int:user_id>/', views.chat_view, name='chat_view'),
path('chat/', include('chat.urls')),
]
# ]

#Add Django site authentication urls (for login, logout, password management)