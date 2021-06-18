from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('olorin', views.olorin, name='olorin'),
    path('aiwendil', views.aiwendil, name='aiwendil'),
    path('alatar', views.alatar, name='alatar'),
    path('curunir', views.curunir, name='curunir'),
    path('getSensorValues', views.getSensorValues, name='getSensorValues'),
    path('setCoil', views.setCoil, name='setCoil'),
]