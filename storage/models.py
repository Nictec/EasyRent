from __future__ import unicode_literals

from django.db import models 
from storage.choices import *

# Create your models here.
class Equipment(models.Model): 
    name = models.CharField(max_length=30) 
    fabricator = models.CharField(max_length=30, default='-') 
    storeplace = models.IntegerField() 
    labor = models.CharField(max_length=1, choices=labor_choices) 
    event = models.ManyToManyField('Order', blank = True, through= 'Assignment', through_fields=('Equipment', 'Order')) 
    max_quantity = models.IntegerField(default=1, null = True) 
    status = models.CharField(max_length=8, choices = STATUS_CHOICES, default = 'im Lager')
    
   
   
   
    def __str__(self): 
        return self.name 
    
    


class client(models.Model): 
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
    city = models.CharField(max_length=30) 
    street= models.CharField(max_length=30)
    date = models.DateField() 
    GuestNumber = models.IntegerField() 
    description = models.TextField() 
    client = models.ForeignKey("client", on_delete=models.CASCADE, blank = True, null = True) 
    status = models.CharField(max_length=30, choices=order_choices, default='glyphicon glyphicon-remove') 
    
    def __str__(self): 
        return self.name
    
class Assignment(models.Model): 
    Equipment = models.ForeignKey('Equipment',  on_delete=models.CASCADE) 
    Order = models.ForeignKey('Order',  on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField(default=1)
    
    
     
    
    
   