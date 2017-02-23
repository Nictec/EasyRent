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
    class Meta:
        model = Equipment
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
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
    #assignments = AssignmentSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = '__all__'

class ShelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelf
        fields = ('id', 'name')
