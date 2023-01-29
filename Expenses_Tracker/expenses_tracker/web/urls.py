from django.urls import path

from .views import home, create_expenses, edit_expense, delete_expense, show_profile, edit_profile, delete_profile, \
    create_profile

urlpatterns = [
    path('',home,name='home'),

    path('create/',create_expenses,name='create_expenses'),
    path('edit/<int:pk>',edit_expense,name='edit_expense'),
    path('delete/<int:pk>/',delete_expense,name='delete_expense'),

    path('profile/',show_profile,name='show_profile'),
    path('profile/create/',create_profile,name='create_profile'),
    path('profile/edit/',edit_profile,name='edit_profile'),
    path('profile/delete/',delete_profile,name='delete_profile'),

]