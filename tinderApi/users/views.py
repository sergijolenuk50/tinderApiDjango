# from rest_framework_simplejwt.views import TokenObtainPairView  
# from .models import CustomUser  # Імпортуйте вашу кастомну модель користувача  


from django.shortcuts import render

# Создаем здесь представления. 
from rest_framework import generics  
from .models import CustomUser  
from .serializers import CustomUserSerializer  
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  
from rest_framework.permissions import IsAuthenticated  
from rest_framework.exceptions import ValidationError  
from rest_framework import serializers  
from rest_framework_simplejwt.views import TokenRefreshView  
from rest_framework.response import Response  

class UserCreateView(generics.CreateAPIView):  
    queryset = CustomUser.objects.all()  
    serializer_class = CustomUserSerializer  
    # permission_classes = [IsAuthenticated]  


class ProtectedView(generics.ListAPIView):  
    queryset = CustomUser.objects.all()  
    serializer_class = CustomUserSerializer  
    permission_classes = [IsAuthenticated]  


# class MyTokenObtainPairView(TokenObtainPairView):  
#     # Можна додати свою кастомізацію тут, якщо потрібно  
#     pass  

# # Додатково, якщо хочете реалізувати рефреш токенів  
# class MyTokenRefreshView(TokenRefreshView):  
#     pass  


class MyTokenObtainPairSerializer(serializers.Serializer):  
    email = serializers.EmailField()  
    password = serializers.CharField()  

    def validate(self, attrs):  
        # Ваша логіка для валідації  
        user = CustomUser.objects.filter(email=attrs['email']).first()  
        if user is None or not user.check_password(attrs['password']):  
            raise ValidationError('Неправильні облікові дані.')  

        # Додаткова валідація про активність користувача  
        if not user.is_active:  
            raise ValidationError('Користувач неактивний.')  

        return attrs  


class MyTokenObtainPairView(TokenObtainPairView):  
    serializer_class = MyTokenObtainPairSerializer  

    def post(self, request, *args, **kwargs):  
        # Додаємо свій обробник POST  
        return super().post(request, *args, **kwargs)  
    


class MyTokenRefreshView(TokenRefreshView):  
    
    def post(self, request, *args, **kwargs):  
        # Логування запиту на оновлення токена  
        print(f'Token refresh requested by: {request.user.email}')  
        
        # Викликаємо стандартну функціональність для оновлення токена  
        return super().post(request, *args, **kwargs)








# class LoginView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")
#         user = authenticate(username=username, password=password)

#         if user:
#             if api_settings.UPDATE_LAST_LOGIN:
#                 update_last_login(None, user)

#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 "refresh": str(refresh),
#                 "access": str(refresh.access_token),
#             }, status=200)

#         return Response({"error": "Неправильне ім'я користувача або пароль."}, status=400)