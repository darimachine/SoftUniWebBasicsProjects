from django.shortcuts import redirect, render
from ..helpers import get_profile
from ..models import PetPhoto


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

def create_pet_photo(request):
    return render(request,'photo_create.html')

def edit_pet_photo(request):
    return render(request,'photo_edit.html')