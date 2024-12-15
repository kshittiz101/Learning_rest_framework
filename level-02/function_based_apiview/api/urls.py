from django.urls import path
from .views import task_list, task_detail
urlpatterns = [
    path('task-list', task_list, name='task-list'),
    path('task-detail/<int:id>/', task_detail, name='task-detail'),
]
