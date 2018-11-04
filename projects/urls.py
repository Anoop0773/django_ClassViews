from django.urls import path
from .views import *

urlpatterns = [
   
    path('create-project',CreateProject.as_view(),name = "create_project"),
    path('list-project',ListProject.as_view(),name = "list_project"),
    path('save-project',SaveProject,name = "save_project"),
    path('get-project',GetProject,name = "get_project"),
    path('delete-project',DeleteProject,name = "delete_project"),
    path('project/<int:pk>/',DetailProject.as_view(),name = "detail_project"),
   
]
