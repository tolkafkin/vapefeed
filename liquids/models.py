from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Liquid(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название жидкости')
    manufacturer = models.ForeignKey('ManufacturerLiquid', on_delete=models.CASCADE,
                                     verbose_name='Изготовитель жидкости')
    strength = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],
                                                verbose_name='Крепкость')
    cold = models.BooleanField(default=False, verbose_name='Холодок')
    taste = models.CharField(max_length=200, verbose_name='Вкус')

    def __str__(self):
        return f'{self.name} - {self.taste}'

    class Meta:
        verbose_name = 'Жидкость'
        verbose_name_plural = 'Жидкости'


class ManufacturerLiquid(models.Model):
    brand_name = models.CharField(max_length=200, verbose_name='Название изготовителя жидкости')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = 'Изготовитель жидкости'
        verbose_name_plural = 'Изготовители жидкости'
