from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('myForms/', views.forms, name="myForms"),
    path('profile/', views.profile, name="profile"),
    path('videos/', views.videos, name="videos"),
    path('test/', views.test, name="test"),
]