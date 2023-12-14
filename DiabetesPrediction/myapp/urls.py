from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Predict/', views.Predict, name='Predict'),
    path('Predict/result', views.result, name='result'),
]