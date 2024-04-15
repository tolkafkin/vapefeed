from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class User(AbstractUser):

    SIMPLE_USER = 'simple_user'
    MODERATOR = 'moderator'
    ADMINISTRATOR = 'administrator'

    ROLE_CHOICES = [
        (SIMPLE_USER, 'пользователь'),
        (MODERATOR, 'модератор'),
        (ADMINISTRATOR, 'администратор'),
    ]

    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(100)],
                                           verbose_name='Возраст пользователя')
    role = models.CharField(max_length=50, choices=ROLE_CHOICES,
                            default=SIMPLE_USER, verbose_name='Роль пользователя')
