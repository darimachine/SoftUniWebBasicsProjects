from django.shortcuts import render, redirect
from ..helpers import get_profile
from ..models import PetPhoto


def home(request):
    context = {
        'hide_nav_items':True,
    }

    return render(request,'home_page.html',context)

def show_dashboard(request):
    profile = get_profile()
    if not profile:
        return redirect('401_error.html')
    pet_photos=set(PetPhoto.objects.prefetch_related('tagged_pets').filter(tagged_pets__user_profile=profile))
    context = {
        'pet_photos':pet_photos,
    }
    return render(request,'dashboard.html',context)