from django.db import models


class Vape(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название девайса')
    manufacturer = models.ForeignKey('ManufacturerVape', on_delete=models.CASCADE, related_name='vapes',
                                     verbose_name='Изготовитель девайса')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вэйп'
        verbose_name_plural = 'Вэйпы'


class ManufacturerVape(models.Model):
    brand_name = models.CharField(max_length=200, verbose_name='Название изготовителя девайса')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = 'Изготовитель вэйпа'
        verbose_name_plural = 'Изготовители вэйпа'


class VapeProfile(models.Model):
    profile = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name='vape_profiles',
                                verbose_name='Профиль пользователя')
    vape = models.ForeignKey('Vape', on_delete=models.CASCADE, verbose_name='Вэйп')
    body = models.TextField(blank=True, null=True, verbose_name='Статья')

    def __str__(self):
        return f'{self.profile} : {self.vape}'

    class Meta:
        verbose_name = 'Вэйп-профайл'
        verbose_name_plural = 'Вэйп-профайлы'
