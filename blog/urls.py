from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('login/', views.login),
    path('sign-up/', views.sign_up),
]
