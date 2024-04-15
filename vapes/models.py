from django.db import models


class Vape(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название девайса')
    manufacturer = models.ForeignKey('ManufacturerVape', on_delete=models.CASCADE,
                                     verbose_name='Изготовитель девайса')


class ManufacturerVape(models.Model):
    brand_name = models.CharField(max_length=200, verbose_name='Название изготовителя девайса')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


class VapeProfile(models.Model):
    profile = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name='vape_profiles',
                                verbose_name='Профиль пользователя')
    vape = models.ForeignKey('Vape', on_delete=models.CASCADE, verbose_name='Вэйп')
    body = models.TextField(blank=True, null=True, verbose_name='Статья')
