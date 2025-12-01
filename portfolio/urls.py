from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('education/', views.education, name='education'),
    path('experience/', views.experience, name='experience'),
    path('skills/', views.skills, name='skills'),
    path('hobbies/', views.hobbies, name='hobbies'),
    path('download_cv/', views.download_cv, name='download_cv'),
]