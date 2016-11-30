# -*- coding: utf-8 -*-
from django import forms 
from .models import Equipment, Order  
from storage.choices import *


 
class neweqForm(forms.ModelForm): 
   
    
    name = forms.CharField(label="Name") 
    fabricator = forms.CharField(label="Hersteller") 
    storeplace = forms.IntegerField(label="Regal") 
    labour = forms.ChoiceField(label = "Gewerk", choices=labor_choices) 
    quantity = forms.IntegerField(label = "Anzahl")
    
     
    
    class Meta: 
        model = Equipment 
        fields =['name', 'fabricator', 'storeplace', 'labour', 'quantity'] 
 
 


class neweventForm(forms.ModelForm): 
    
    name = forms.CharField(label="Name") 
    Type = forms.ChoiceField(label="Art", choices=TYPE_CHOICES ) 
    city = forms.CharField(label="Ort") 
    street = forms.CharField(label="Straße") 
    date = forms.DateField(label="Datum") 
    GuestNumber = forms.IntegerField(label="Gästeanzahl")
    description = forms.CharField(label="Beschreibung", widget=forms.Textarea)
    
    class Meta: 
        model = Order 
        fields =['name', 'Type', 'city', 'street', 'date', 'GuestNumber', 'description'] 

    
class FilterForm(forms.Form): 
    
    filter = forms.ChoiceField(choices=labor_choices) 
    
class quantityForm(forms.Form): 
    quantity = forms.IntegerField(label="benötigte Anzahl") 
    
    
class login_form(forms.Form): 
    email = forms.CharField(label='email')
    password = forms.CharField(widget=forms.PasswordInput, label='password') 
    

    