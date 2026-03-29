from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects'),
    path('education/', views.education, name='education'),
    path('certifications/', views.certifications, name='certifications'),
    path('achievements/', views.achievements, name='achievements'),
    path('contact/', views.contact, name='contact'),
]
