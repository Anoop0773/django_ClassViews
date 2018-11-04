from django.urls import path
from .views import *

urlpatterns = [
   
    
    path('list-task',ListTask.as_view(),name = "list_task"),
    path('save-task',SaveTask,name = 'save_task'),
    path('get-task',GetTask,name = "get_task"),
    path('delete-task',DeleteTask,name = "delete_task"),
    path('task/<int:pk>/',DetailTask.as_view(),name = "detail_task"),
   
]
