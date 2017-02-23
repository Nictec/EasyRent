from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import *


class EquipmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Equipment
		fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
	equipment_data = EquipmentSerializer(read_only=True, source="equipment")
	class Meta:
		model = Assignment
		fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
	assignment = AssignmentSerializer(many=True, read_only=True)
	class Meta:
		model = Order
		#fields = '__all__'
		exclude = ('assignments',)

class ShelfSerializer(serializers.ModelSerializer):
	class Meta:
		model = Shelf
		fields = ('id', 'name')

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
