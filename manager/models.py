from __future__ import unicode_literals

from django.db import models 
from storage.choices import *

# Create your models here.
class Equipment(models.Model): 
    name = models.CharField(max_length=30) 
    fabricator = models.CharField(max_length=30, default='-') 
    beschreibung = models.CharField(max_length=1000, blank=True) 
    Image = models.ImageField(upload_to='product_pics', default="../Media/product_pics/no_image.png")
    storeplace = models.ForeignKey("shelf", on_delete=models.CASCADE) 
    labor = models.CharField(max_length=1, choices=labor_choices) 
    orders = models.ManyToManyField('Order', blank = True, through= 'Assignment', through_fields=('Equipment', 'Order')) 
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
    city = models.CharField(max_length=30, null=True, blank=True) 
    street= models.CharField(max_length=30, null=True, blank=True)
    dateStart = models.DateField(null=True) 
    dateEnd = models.DateField(null=True) 
    GuestNumber = models.IntegerField(null=True) 
    description = models.TextField() 
    client = models.ForeignKey("client", on_delete=models.CASCADE, blank = True, null = True) 
    status = models.CharField(max_length=30, choices=order_choices, default='notOK') 
    
    def __str__(self): 
        return self.name
    
class Assignment(models.Model): 
    Equipment = models.ForeignKey('Equipment', related_name = "order",  on_delete=models.CASCADE) 
    Order = models.ForeignKey('Order',  on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField(default=1) 
    
class shelf(models.Model): 
    name = models.CharField(max_length=100)
    def __str__(self): 
        return self.name
    
     
    
    
   