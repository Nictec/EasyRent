from django.conf.urls import url, include 	
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin 
from . import views 
from storage.views import storage, storageupdate, storagedelete, Order_view, eqlist, ass_detail, userlist

urlpatterns = [
    url(r'^$', views.index, name='index'), 
    url(r'^login/$', views.loginsys, name='login'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^equipment/$', storage.as_view(), name='storage'), 
    url(r'^update_eq(?P<pk>\d+)/$', storageupdate.as_view(), name="storageupdate"), 
     url(r'^deleteeq/(?P<pk>\d+)/$', storagedelete.as_view(), name='storagedelete'),
    url(r'^clients/',userlist.as_view() , name='clients'), 
    url(r'events/', Order_view.as_view(), name='Order'), 
    url(r'^bills/', views.bills, name='bills'), 
    url(r'^reservations/', views.reservations, name='reservations'), 
    url(r'^neweq/', views.neweq, name='neweq'), 
    url(r'^newevent/$', views.new_Order, name="newevent"), 
    url(r'^chose/$', eqlist.as_view(), name="eqlist"), 
    url(r'^eqadd/$', views.eqadd, name='eqadd'), 
    url(r'^Order_details(?P<pk>\d+)/$',ass_detail.as_view(), name='ass_detail'), 
    url(r'delsession/', views.del_session, name="delete_session"), 
    url(r'picklist/(?P<pk>\d+)', views.picklist, name="picklist"), 
    url(r'details/(?P<pk>\d+)', views.details, name="details"), 
    url(r'logout/', views.logout_view, name = "logout"),
    url(r'statusSet/', views.SetOrder, name="SetOrder"),
#    url(r'debugs/', jlist.as_view()), 
    url(r'^config/', views.admin, name = "conf"),
    url(r'^api-auth-token/', obtain_auth_token),
    
    
]

