from django.shortcuts import render 
from django.contrib.auth.models import User, Group
from manager.serializers import *
from rest_framework import generics 
from rest_framework import viewsets 



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
    

    
    
    
    
