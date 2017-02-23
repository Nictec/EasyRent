from __future__ import unicode_literals

from django.db import models
from storage.choices import *

# Create your models here.
class Equipment(models.Model):
    name = models.CharField(max_length=30)
    fabricator = models.CharField(max_length=30, default='-')
    beschreibung = models.CharField(max_length=1000, blank=True)
    labor = models.CharField(max_length=1, choices=labor_choices)
    max_quantity = models.IntegerField(default=1, null = True)
    status = models.CharField(max_length=8, choices = STATUS_CHOICES, default = 'im Lager')
    storeplace = models.ForeignKey("shelf", on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Client(models.Model):
    firstname = models.CharField(max_length=30)
    secondname = models.CharField(max_length=30)
    email = models.EmailField()
    post_code = models.IntegerField()
    city = models.CharField(max_length=30)
    street= models.CharField(max_length=30)

    def __str__(self):
        return "%s %s" % (self.firstname, self.secondname)



class Order(models.Model):
    name = models.CharField(max_length=30)
    Type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default='Rental',
        )
    city = models.CharField(max_length=30, null=True, blank=True)
    street= models.CharField(max_length=30, null=True, blank=True)
    dateStart = models.DateField(null=True)
    dateEnd = models.DateField(null=True)
    GuestNumber = models.IntegerField(null=True)
    description = models.TextField()
    status = models.CharField(max_length=30, choices=order_choices, default='notOK')
    client = models.ForeignKey("client", on_delete=models.CASCADE, blank = True, null = True)
    assignments = models.ManyToManyField('Equipment', blank = True, through= 'Assignment', through_fields=('order', 'equipment'))

    def __str__(self):
        return self.name

class Assignment(models.Model):
    order = models.ForeignKey('Order', related_name = "assignment",  on_delete=models.CASCADE)
    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Shelf(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name





