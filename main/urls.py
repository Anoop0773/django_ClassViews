from django.urls import path
from .views import *

urlpatterns = [
   
    path('',Login.as_view(),name = "login"),
    path('dashboard',Dashboard.as_view(),name = "dashboard"),
    path('logout/', Logout, name='logout'),
]
