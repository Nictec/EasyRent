from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from django.conf import settings
from djradicale.views import WellKnownView
from django.views.generic import RedirectView
from django.conf import settings
from rest_framework.authtoken import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', views.obtain_auth_token),
    url(r'^users/', include('users.urls')),
    url(r'^', include('manager.urls'), name="manager"),

]
