from django.urls import path
from . import views


urlpatterns = [
    path('api2', views.index_page),
    path('predict-titanic-survival', views.predict_titanic_survival),
]
