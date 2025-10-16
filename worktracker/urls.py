from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.taskList, name='task_list'),
    path('tasks/<int:pk>/', views.taskDetail, name='task_detail'),
    path('employees/', views.employeeList, name='employee_list'),
    path('employees/<int:pk>/', views.employeeDetail, name='employee_detail'),
    path('assigned/', views.assignedTasksList, name='assigned_tasks_list'),
    # Add more paths as needed
]