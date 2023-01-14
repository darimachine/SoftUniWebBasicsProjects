from django.urls import path
from .views import home, show_dashboard, show_profile, show_pet_photo_details, like_pet

urlpatterns = [
    path('',home,name='index'),
    path('dashboard/',show_dashboard,name='dashboard'),
    path('profile/',show_profile,name='profile'),
    path('photo/details/<int:pk>',show_pet_photo_details,name='pet_photo_details'),
    path('photo/like/<int:pk>/',like_pet,name='like_pet_photo')

]