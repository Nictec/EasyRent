from django.contrib import admin
from .models import Equipment, Client, Order, Assignment, Shelf

# Register your models here.
class AssignmentInline(admin.TabularInline):
    model = Assignment
    extra = 1

class EquipmentAdmin(admin.ModelAdmin):
    inlines = (AssignmentInline, )

admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Shelf)
