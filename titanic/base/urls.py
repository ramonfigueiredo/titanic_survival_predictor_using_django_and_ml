from django.urls import include, path
from rest_framework import routers

from .views import home, result, UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('predict/', home, name='home'),
    path('predict/result/', result, name='result'),
    # Wire up the API using automatic URL routing.
    # Additionally, include login URLs for the browsable API.
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
