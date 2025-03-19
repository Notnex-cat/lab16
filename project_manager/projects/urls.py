# projects/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('project/create/', views.create_project, name='create_project'),
    path('project/<int:project_id>/task/create/', views.create_task, name='create_task'),
]
