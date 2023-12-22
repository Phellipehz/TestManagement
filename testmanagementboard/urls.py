
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects', views.project_list, name='project_list'),
]