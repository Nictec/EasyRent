from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import *


class EquipmentSerializer(serializers.ModelSerializer):
	avail_quantity = serializers.SerializerMethodField()
	class Meta:
		model = Equipment
		fields = '__all__'

	def get_avail_quantity(self, obj):
		assigned_sum = 0
		assignments = Assignment.objects.filter(equipment=obj.id, active=True)
		for assignment in assignments:
			assigned_sum += assignment.quantity
		return obj.max_quantity - assigned_sum

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
		fields = ('__all__')

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
