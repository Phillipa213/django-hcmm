from django.urls import path
from . import views

app_name = 'collaborative_working'

urlpatterns = [
    path('', views.home, name='home'),  # Ensure this pattern exists
    path('', views.task_list, name='task_list'),
    path('<int:pk>/', views.task_detail, name='task_detail'),
    path('create/', views.task_create, name='task_create'),
    path('add/', views.add_task, name='add_task'),
    path('update/<int:pk>/', views.update_task, name='update_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
]
