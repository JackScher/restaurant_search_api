from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "dishes"

    def __str__(self):
        return f'{self.name}'
