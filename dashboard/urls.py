from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

 # URL for signup
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
 ]