from django.db import models
from django.contrib.auth.models import User


# Create your models here.
MEAL_TYPE = (
    ('starters', 'Starters'),
    ('salads', 'Salads'),
    ('main_dishes', 'Main Dishes'),
    ('desserts', 'Desserts')

)

STATUS = (
    (0, 'Available'),
    (1, 'Unavailable')

)


class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=200, choices=MEAL_TYPE)
    auther = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.CharField(max_length=200, choices=STATUS)
    # date_created = models. DateTimeField(auto_now_add=True)
    # date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal