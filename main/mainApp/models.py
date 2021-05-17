
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('device_list_by_category',
                       args=[self.slug])


class Device(models.Model):

    name = models.CharField(max_length=200,
                            verbose_name="Название",
                            null=True)

    category = models.ForeignKey('Category',
                                 related_name='products',
                                 on_delete=models.CASCADE,
                                 verbose_name="Тип",)

    address = models.TextField(verbose_name="Адрес",
                               blank=True,
                               null=False)

    latitude = models.DecimalField(max_digits=20,
                                   decimal_places=6,
                                   verbose_name="Широта",
                                   null=True)  # Широта

    longitude = models.DecimalField(max_digits=20,
                                    decimal_places=6,
                                    verbose_name="Долгота",
                                    null=True)  # Долгота

    radius = models.IntegerField(verbose_name="Радиус зоны звукопокрытия (м)",
                                 null=True)  # Радиус зоны звукопокрытия в метрах

    slug = models.SlugField(max_length=200, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Девайс'
        verbose_name_plural = 'Девайсы'

    def get_absolute_url(self):
        return reverse('device_item',
                       args=[self.slug])

