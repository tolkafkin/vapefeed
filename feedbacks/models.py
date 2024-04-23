from django.db import models


class Feedback(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название отзыва')
    vape_profile = models.ForeignKey('vapes.VapeProfile', related_name='feedbacks',on_delete=models.CASCADE,
                                     verbose_name='Вэйп')
    liquid = models.ForeignKey('liquids.Liquid', on_delete=models.CASCADE, related_name='feedbacks',
                               verbose_name='Жидкость')
    body = models.TextField(blank=True, verbose_name='Текст')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.title
