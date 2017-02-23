from django.conf.urls import url, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from . import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'group', views.GroupViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'equipment', views.EquipmentViewSet)
router.register(r'assignment', views.AssignmentViewSet)
router.register(r'client', views.ClientViewSet)
router.register(r'shelf', views.ShelfViewSet)


urlpatterns = router.urls
urlpatterns.append(url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')))

#Media files
urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)
