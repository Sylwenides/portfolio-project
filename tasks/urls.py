from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.tasks, name="list"),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
]