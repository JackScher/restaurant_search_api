from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.name}'
