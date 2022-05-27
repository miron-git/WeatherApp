from django.db import models

class City(models.Model):
    name = models.CharField(max_length=30, verbose_name = 'Название')

    def __str__(self):
        return self.name

class Weather(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['city',]