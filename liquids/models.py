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


class ManufacturerLiquid(models.Model):
    brand_name = models.CharField(max_length=200, verbose_name='Название изготовителя жидкости')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')