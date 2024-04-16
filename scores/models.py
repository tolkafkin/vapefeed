from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

user_model = get_user_model()


class Score(models.Model):
    user = models.ForeignKey(user_model, on_delete=models.CASCADE, related_name='scores', verbose_name='Пользователь')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    value = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],
                                             verbose_name='Рейтинг')

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

    def __str__(self):
        return f'{self.user.username} - {self.value}'


class UserFeedbackScore(models.Model):
    score = models.ForeignKey('Score', on_delete=models.CASCADE, verbose_name='Рейтинг пользователя')
    feedback = models.ForeignKey('feedbacks.Feedback', related_name='users_feedbacks', on_delete=models.CASCADE,
                                 verbose_name='Отзыв')

    class Meta:
        verbose_name = 'Рейтинг отзыва'
        verbose_name_plural = 'Рейтинги отзывов'

    def __str__(self):
        return f'{self.score} : {self.feedback.title}'


class LiquidFeedbackScore(models.Model):
    score = models.ForeignKey('Score', on_delete=models.CASCADE, verbose_name='Рейтинг пользователя')
    liquid = models.ForeignKey('liquids.Liquid', on_delete=models.CASCADE, related_name='liquids_feedbacks',
                               verbose_name='Жидкость')

    class Meta:
        verbose_name = 'Рейтинг жидкости'
        verbose_name_plural = 'Рейтинги жидкостей'

    def __str__(self):
        return f'{self.score} : {self.liquid.taste}'
