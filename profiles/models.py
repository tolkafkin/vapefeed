from django.contrib.auth import get_user_model
from django.db import models

user_model = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(user_model, on_delete=models.CASCADE, related_name='profile',
                                verbose_name='Пользователь')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='user_photo', blank=True, null=True, verbose_name='Фото пользователя')
