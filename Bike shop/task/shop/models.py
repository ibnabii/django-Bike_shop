from django.contrib.auth.models import User
from django.db import models

default_length = 20  # default length of char field


class Frame(models.Model):
    color = models.CharField(max_length=default_length)
    quantity = models.IntegerField()

    def __str__(self):
        return self.color


class Seat(models.Model):
    color = models.CharField(max_length=default_length)
    quantity = models.IntegerField()

    def __str__(self):
        return self.color


class Tire(models.Model):
    type = models.CharField(max_length=default_length)
    quantity = models.IntegerField()

    def __str__(self):
        return self.type


class Basket(models.Model):
    quantity = models.IntegerField()


class Bike(models.Model):
    name = models.CharField(max_length=default_length)
    description = models.TextField()
    has_basket = models.BooleanField(default=False)
    frame = models.ForeignKey(Frame, on_delete=models.PROTECT)
    tire = models.ForeignKey(Tire, on_delete=models.PROTECT)
    seat = models.ForeignKey(Seat, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUSES = [('P', 'pending'), ('R', 'ready')]
    bike = models.ForeignKey(Bike, on_delete=models.PROTECT)
    name = models.CharField(max_length=default_length)
    surname = models.CharField(max_length=default_length)
    phone_number = models.CharField(max_length=default_length)
    status = models.CharField(max_length=1, choices=STATUSES, default='pending')

list_of_models = [Frame, Seat, Tire, Basket, Bike, Order
                  ]