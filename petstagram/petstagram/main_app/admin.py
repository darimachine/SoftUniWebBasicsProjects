from django.contrib import admin
from .models import Profile,Pet
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass
