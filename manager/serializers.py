from rest_framework import serializers  
from django.contrib.auth.models import User, Group
from .models import * 

        
class AssignmentSerializer(serializers.HyperlinkedModelSerializer): 
    id = serializers.ReadOnlyField(source = 'Order.id') 
    name = serializers.ReadOnlyField(source = 'Order.name') 
    
    class Meta:
        model = Assignment 
        fields = ('id', 'name', 'quantity') 
        
        
class EquipmentSerializer(serializers.ModelSerializer): 
    order = AssignmentSerializer( many = True) 
    Image = serializers.ImageField(allow_empty_file=True)
    class Meta: 
        model = Equipment 
        fields = '__all__' 
    
    def create(self, data):
        #order = Order.objects.get(pk=18)
        order = data.pop("order") # TODO: add support for orders
        instance = Equipment.objects.create(**data)
        #instance.event.add(event)
        #Assignment.objects.create(Order=order, Equipment=instance)
        return instance 
    
    def update(self, instance, data): 
        if data.get("order"):
            order = data.pop("order") # TODO: add support for orders
        for attr, value in data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    
#    def to_representation(self, instance):
#        representation = super(EquipmentSerializer, self).to_representation(instance)
#        representation['assigment'] = AssignmentSerializer(instance.order.all(), many=True).data
#        
#        return representation 
        
        
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

class OrderSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Order 
        fields = '__all__' 
        
class ShelfSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = shelf 
        fields = ('id', 'name')
        
        
       
        