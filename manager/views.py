from django.shortcuts import render 
from django.contrib.auth.models import User, Group
from manager.serializers import *
from rest_framework import generics 
from rest_framework import viewsets 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.views import APIView  
from django.forms.models import model_to_dict



class OrderSetDetails(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Order.objects.all() 
    serializer_class = OrderSerializer 
    
class OrderSetList(generics.ListCreateAPIView): 
    queryset = Order.objects.all() 
    serializer_class = OrderSerializer 

class EquipmentSetDetails(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Equipment.objects.all() 
    serializer_class = EquipmentSerializer 
    
class EquipmentSetList(generics.ListCreateAPIView): 
    queryset = Equipment.objects.all() 
    serializer_class = EquipmentSerializer
    

class UserViewSet(viewsets.ModelViewSet):
 
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer 
    
class ClientList(generics.ListCreateAPIView): 
    queryset = client.objects.all() 
    serializer_class = ClientSerializer 
    
class ShelfList(generics.ListCreateAPIView): 
    queryset = shelf.objects.all() 
    serializer_class = ShelfSerializer 
    
class ShelfDeatil(generics.RetrieveUpdateDestroyAPIView): 
    queryset = shelf.objects.all() 
    serializer_class = ShelfSerializer
    

    
    
    
    
