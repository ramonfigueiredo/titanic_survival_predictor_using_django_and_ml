from django.urls import path, include
from rest_framework import routers

from .views import predict_titanic_survival, UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('predict-titanic-survival', predict_titanic_survival),
    # Wire up the API using automatic URL routing.
    # Additionally, include login URLs for the browsable API.
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
