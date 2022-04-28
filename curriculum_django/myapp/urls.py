from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="HOME"),
    path('ABOUT ME', views.about_me, name="ABOUT ME"),
    path('graduation/', views.graduation, name="GRADUATION"),
    path('certifications/', views.certifications, name="CERTIFICATIONS"),
    path('work_experience/', views.work_experience, name="EXPERIENCE"),
    path('contact/', views.contact, name="CONTACT"),
    path('resume/', views.resume, name="RESUME"),
]