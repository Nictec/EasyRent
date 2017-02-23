from django.contrib import admin
from .models import Equipment, Client, Order, Assignment, Shelf

# Register your models here.
class AssignmentInline(admin.TabularInline):
    model = Assignment
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = (AssignmentInline, )

admin.site.register(Equipment)
admin.site.register(Order, OrderAdmin)
admin.site.register(Client)
admin.site.register(Shelf)
