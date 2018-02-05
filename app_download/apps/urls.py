from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('packages', views.packages, name="packages"),
    path('setups', views.exes, name="setups"),
]