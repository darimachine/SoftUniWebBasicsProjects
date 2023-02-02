
from django.urls import path,include
from .views import show_index, show_catalogue, create_profile, profile_details, edit_profile, delete_profile, \
    create_car, car_details, edit_car, delete_car

urlpatterns = [
    #index and catalogue
    path('',show_index,name='index'),
    path('catalogue/',show_catalogue,name='catalogue'),

    #profile
    path('profile/create/',create_profile,name='create_profile'),
    path('profile/details/',profile_details,name='profile_details'),
    path('profile/edit/',edit_profile,name='edit_profile'),
    path('profile/delete/',delete_profile,name='delete_profile'),

    #car
    path('car/create/',create_car,name='create_car'),
    path('profile/<int:pk>/details/',car_details,name='car_details'),
    path('profile/<int:pk>/edit/',edit_car,name='edit_car'),
    path('profile/<int:pk>/delete/',delete_car,name='delete_car'),

]