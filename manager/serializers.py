from rest_framework import serializers  
from django.contrib.auth.models import User, Group
from storage.models import * 

        
class AssignmentSerializer(serializers.HyperlinkedModelSerializer): 
    id = serializers.ReadOnlyField(source = 'Order.id') 
    name = serializers.ReadOnlyField(source = 'Order.name') 
    
    class Meta:
        model = Assignment 
        fields = ('id', 'name', 'quantity') 
        

class OrderSerializer(serializers.ModelSerializer):     
    class Meta: 
        model = Order 
        fields = '__all__' 
        
class EquipmentSerializer(serializers.ModelSerializer): 
    event = AssignmentSerializer(source= 'assignment_set', many = True)
    class Meta: 
        model = Equipment 
        fields = '__all__' 
        
        
class ClientSerializer(serializers.ModelSerializer): 
    
    class Meta: 
        model = client 
        fields = '__all__' 
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name') 
        
        
       
        