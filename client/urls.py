from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.app, name = 'main'),
    
]