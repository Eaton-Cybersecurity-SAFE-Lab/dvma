from django.urls import path

from . import views

urlpatterns = [
    path('getsensorlevels', views.getsensorlevels, name='getsensorlevels'),
]