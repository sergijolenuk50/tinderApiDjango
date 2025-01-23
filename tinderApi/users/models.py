# from django.db import models


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin  
from django.db import models  


class CustomUserManager(BaseUserManager):  

    def create_user(self, email, password=None, **extra_fields):  
        if not email:  
            raise ValueError('Email address must be provided')  
        email = self.normalize_email(email)  
        user = self.model(email=email, **extra_fields)  
        user.set_password(password)  
        user.save(using=self._db)  
        return user  

    def create_superuser(self, email, password=None, **extra_fields):  
        extra_fields.setdefault('is_staff', True)  
        extra_fields.setdefault('is_superuser', True)  

        return self.create_user(email, password, **extra_fields)  


class CustomUser(AbstractBaseUser, PermissionsMixin):  
    email = models.EmailField(unique=True)  
    first_name = models.CharField(max_length=30, blank=True)  
    last_name = models.CharField(max_length=30, blank=True)  
    is_active = models.BooleanField(default=True)  
    is_staff = models.BooleanField(default=False)  

    objects = CustomUserManager()  

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = []  

    def __str__(self):  
        return self.email




# Create your models here.
# from django.contrib.auth.models import AbstractUser  

# class CustomUser(AbstractUser):  
#     # Інші поля, які ви хочете додати
#     email = models.EmailField(unique=True)  
#     full_name = models.CharField(max_length=255, blank=True, null=True)  
#     avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)  
#     bio = models.TextField(max_length=500, blank=True)  
#     display_name = models.CharField(max_length=255, blank=True, null=True)   


#     # def __str__(self):
#     #     return self.username

