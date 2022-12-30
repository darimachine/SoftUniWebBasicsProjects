
from django.urls import path,include
from .views import department_details, list_departments
urlpatterns = [
    path('',department_details,name='details'),
    path('<int:id>/',list_departments,name='list'),
]