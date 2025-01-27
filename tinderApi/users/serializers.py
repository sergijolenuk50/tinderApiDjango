from rest_framework import serializers  
from .models import CustomUser  

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'password']
    
    def create(self, validated_data):
        password = validated_data.pop('password')  # Витягуємо пароль з даних
        user = CustomUser(**validated_data)  # Створюємо об'єкт користувача без пароля
        user.set_password(password)  # Хешуємо пароль
        user.save()  # Зберігаємо користувача з хешованим паролем
        return user