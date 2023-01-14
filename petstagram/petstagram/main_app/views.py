from django.shortcuts import render, redirect

# Create your views here.
from .models import Profile,Pet,PetPhoto

def get_profile():
    profiles= Profile.objects.all()
    if profiles:
        return profiles[0]
    return None

def home(request):
    context = {
        'hide_nav_items':True,
    }

    return render(request,'home_page.html',context)

def show_dashboard(request):
    profile = get_profile()
    pet_photos=set(PetPhoto.objects.prefetch_related('tagged_pets').filter(tagged_pets__user_profile=profile))
    context = {
        'pet_photos':pet_photos,
    }
    return render(request,'dashboard.html',context)

def show_profile(request):
    return render(request,'profile_details.html')

def show_pet_photo_details(request,pk):
    pet = PetPhoto.objects.get(id=pk)
    context={
        'pet_photo':pet,
    }
    return render(request,'photo_details.html',context)

def like_pet(request,pk,):
    pet_photo = PetPhoto.objects.prefetch_related('tagged_pets').get(pk=pk)
    pet_photo.likes+=1
    pet_photo.save()
    return redirect('pet_photo_details',pk)