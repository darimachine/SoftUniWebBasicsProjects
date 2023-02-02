from django.core.validators import MinLengthValidator,MinValueValidator
from django.db import models

# Create your models here.
from .validators import YearRange


class Profile(models.Model):
    USERNAME_MAX_LENGHT=10
    USERNAME_MIN_LENGTH=2
    #Age
    AGE_MIN = 18
    #password
    PASSWORD_MAX_LENGTH=30

    FIRST_NAME_MAX_LENGTH=30
    LAST_NAME_MAX_LENGTH = 30
    username = models.CharField(
        max_length=USERNAME_MAX_LENGHT,
        validators=[MinLengthValidator(USERNAME_MIN_LENGTH,'The username must be a minimum of 2 chars'),]
    )
    email = models.EmailField()

    age = models.IntegerField(
        validators=[MinValueValidator(AGE_MIN,'You need to be over 18+'),]
    )
    password=models.CharField(
        max_length=PASSWORD_MAX_LENGTH
    )
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
    )
    image = models.URLField(
        null=True,
        blank=True,
    )
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
class Car(models.Model):
    TYPE_MAX_LENGTH = 10

    MODEL_MAX_LENGTH = 20
    MODEL_MIN_LENGTH = 20

    PRICE_MIN_VALUE = 1

    TYPE_CHOICES = ("Sports Car", "Pickup", "Crossover", "Minibus","Other")
    CHOICES = ((c,c) for c in TYPE_CHOICES)

    type=models.CharField(
        max_length=TYPE_MAX_LENGTH,
        choices=CHOICES
    )

    model = models.CharField(
        max_length=MODEL_MAX_LENGTH,
        validators=[MinLengthValidator(MODEL_MIN_LENGTH),]
    )
    year = models.IntegerField(
        validators=(YearRange,)
    )
    image = models.URLField()

    price= models.FloatField(
        validators=[MinLengthValidator(PRICE_MIN_VALUE,'Cannot be bellow 1'),]
    )