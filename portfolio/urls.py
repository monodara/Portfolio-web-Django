from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('hobbies/', views.hobbies, name='hobbies'),
    path('download_cv/', views.download_cv, name='download_cv'),
]