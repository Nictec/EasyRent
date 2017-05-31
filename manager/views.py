from django.shortcuts import render
from django.contrib.auth.models import User, Group
from manager.serializers import *
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from django.forms.models import model_to_dict



class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.filter(~Q(status='Res'))
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

@api_view(['GET'])
def current_user(request):
    user = request.user
    return Response({
        'id': user.id,
    })
@api_view(['GET'])
def cal(request):
    start = request.GET.get('start')
    end = request.GET.get('end')
    queryset = Order.objects.filter(~Q(status='F'),dateStart__range=[start, end])
    serializer = CalendarSerializer(queryset, many=True)
    return Response(serializer.data)
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

class ShelfViewSet(viewsets.ModelViewSet):
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.filter(status='Res')
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
