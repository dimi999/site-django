from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'tasks'),
    path('home/', views.home, name = 'tasks'),
    path('login/', views.loginPage, name = 'tasks'),
    path('register/', views.registerPage, name = 'tasks'),
    path('features/', views.features, name = 'tasks'),
]