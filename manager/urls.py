from django.conf.urls import url, include
from rest_framework import routers  
from . import views 
from .views import *

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [ 
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), 
    url(r'^orders/all', OrderSetList.as_view(), name='orderlist'), 
    url(r'^orders/(?P<pk>[^/.]+)', OrderSetDetails.as_view(), name='orderdetail'), 
    url(r'^equipment/all', EquipmentSetList.as_view(), name='eqlist'), 
    url(r'^equipment/(?P<pk>[^/.]+)', EquipmentSetDetails.as_view(), name='eqdetail'), 
   
    
    
     
  
]
