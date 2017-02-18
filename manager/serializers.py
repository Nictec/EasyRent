from rest_framework import serializers  
from django.contrib.auth.models import User, Group
from .models import * 

        
class AssignmentSerializer(serializers.HyperlinkedModelSerializer): 
    order = serializers.ReadOnlyField(source = 'Order.id') 
    equipment = serializers.ReadOnlyField(source = 'Equipment.id') 
    
    class Meta:
        model = Assignment 
        fields = ('order', 'equipment', 'quantity') 
        
        
class EquipmentSerializer(serializers.ModelSerializer): 
    assignments = serializers.SerializerMethodField()
    #SerializerMethodField looks for a method get_{name of the field}
    #assignment_orders = serializers.SerializerMethodField()
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

    #this is the method used by SerializerMethodField
    def get_assignments(self, obj):
        assignments = Assignment.objects.filter(Equipment=obj.id)
        #orders = Order.objects.filter(Equipment=obj.id)
        s = AssignmentSerializer(assignments, many=True)
        return s.data
    #def get_assigned_orders(self, obj):
        #it should be possible to query all the assigned orders here and display them
        #similar to getting the assignments above
    
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
    assignments = AssignmentSerializer(many=True, read_only=True)
    class Meta: 
        model = Order 
        fields = '__all__' 
        
class ShelfSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = shelf 
        fields = ('id', 'name')
        
        
       
        
