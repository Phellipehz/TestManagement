
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects', views.project_list, name='project_list'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    #path('update_test_step_status/<int:test_step_id>/<str:new_status>/', update_test_step_status, name='update_test_step_status'),
]