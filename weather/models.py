from django.db import models

class City(models.Model):
    name = models.CharField(max_length=30, verbose_name = 'Название')
    label = models.CharField(max_length=30, verbose_name = 'Значение')

    def __str__(self):
        return self.name