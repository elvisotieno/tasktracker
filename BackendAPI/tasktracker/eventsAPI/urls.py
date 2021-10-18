from django.urls import path
from .views import task_list, detail, current_time, current_task


urlpatterns = [
    path('tasks/', task_list),
    path('detail/<int:pk>/', detail),
    path('current_time/', current_time),
    path('current_task/', current_task),
]