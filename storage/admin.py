from django.contrib import admin 
from .models import Equipment, client, Order, Assignment

# Register your models here. 
class AssignmentInline(admin.TabularInline): 
    model = Assignment 
    extra = 1 
    
class EquipmentAdmin(admin.ModelAdmin): 
    inlines = (AssignmentInline, ) 
    
admin.site.register(Equipment, EquipmentAdmin) 
admin.site.register(client) 
admin.site.register(Order)