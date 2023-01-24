
from django.urls import path,include
from .views import department_details, list_departments, create_employee, edit_employee

urlpatterns = [
    path('',department_details,name='details'),
    path('<int:id>/',list_departments,name='list'),
    path('create/',create_employee,name='create_employee'),
    path('edit/<int:pk>/',edit_employee,name='edit_employee')
]