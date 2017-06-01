from django.conf.urls import url, include
from . import views
from .views import ResetPasswordRequestView, PasswordResetConfirmView

urlpatterns = [
    url(r'^reset_password/', ResetPasswordRequestView.as_view(), name="reset_password"),
    url(r'^reset_password_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(),name='reset_password_confirm'),
]
