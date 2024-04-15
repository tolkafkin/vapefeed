from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

user_model = get_user_model()


class Score(models.Model):
    user = models.ForeignKey(user_model, on_delete=models.CASCADE, verbose_name='Пользователь')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    value = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],
                                             verbose_name='Рейтинг')


class UserFeedbackScore(models.Model):
    score = models.ForeignKey('Score', on_delete=models.CASCADE, verbose_name='Рейтинг пользователя')
    feedback = models.ForeignKey('feedback.Feedback', on_delete=models.CASCADE, verbose_name='Отзыв')


class LiquidFeedbackScore(models.Model):
    score = models.ForeignKey('Score', on_delete=models.CASCADE, verbose_name='Рейтинг пользователя')
    liquid = models.ForeignKey('liquids.Liquids', on_delete=models.CASCADE, verbose_name='Жидкость')
