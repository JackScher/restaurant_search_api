from django.db import models

from restaurants.models import Restaurant


class Menu(models.Model):
    price = models.FloatField()
    date = models.DateField(auto_now_add=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dishes = models.ManyToManyField("dishes.Dish")

    def related_dishes(self):
        return [str(dish) for dish in self.dishes.all()]

    def __str__(self):
        return f'{self.restaurant} menu'
