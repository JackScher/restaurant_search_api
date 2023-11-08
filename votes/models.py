from django.db import models

from employees.models import Employee
from menus.models import Menu


class Vote(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.employee.username} vote'
