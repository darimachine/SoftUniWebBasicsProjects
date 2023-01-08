from django.db import models
from django.core.validators import MinLengthValidator
from .validators import only_letters_validator

# Create your models here.
class Profile(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'
    GENDERS = [(x,x) for x in (MALE,FEMALE,DO_NOT_SHOW)]
    FIRST_NAME_MAX_LENGHT=30
    LAST_NAME_MAX_LENGHT = 30
    FIRST_NAME_MIN_LENGHT = 2
    LAST_NAME_MIN_LENGHT = 2
    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGHT,
                                  validators=[
                                      MinLengthValidator(FIRST_NAME_MIN_LENGHT,'first name must be between 2 and 30'),
                                      only_letters_validator],
                                  )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGHT,
        validators=[
            MinLengthValidator(LAST_NAME_MIN_LENGHT, 'last name must be between 2 and 30'),
            only_letters_validator,
        ],
    )
    picture = models.URLField()
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=True,
        blank=True,
    )
    gender = models.CharField(
        max_length=max(len(gender) for gender,_ in GENDERS),
        null=True,
        blank=True,
        choices=GENDERS,
    )
class Pet(models.Model):
    PET_NAME_MAX_LENGHT=30
    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH='Fish'
    OTHER = 'Other'
    TYPE=[(x,x) for x in (CAT,DOG,BUNNY,PARROT,FISH,OTHER)]
    name =models.CharField(
        max_length=PET_NAME_MAX_LENGHT,
        unique=True
    )
    type = models.CharField(
        max_length=max(len(type) for type,_ in TYPE),
        choices=TYPE
    )
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )