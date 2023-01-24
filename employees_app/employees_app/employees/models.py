from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class AuditEntity(models.Model):
    created_on = models.DateField(
        auto_now_add=True
    )
    update_on = models.DateField(
        auto_now=True
    )
    class Meta:
        abstract = True
class Department(AuditEntity):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Employee(models.Model):
    SOFTWARE_DEVELOPER = 1
    QA_ENGINEER=2
    DEVOPS_SPECIALIST = 3

    SOFT_UNI = 'Softuni'
    GOOGLE = 'Google'
    FACEBOOK = 'FACEBOOK'
    COMPANIES=(
        SOFT_UNI,
        GOOGLE,
        FACEBOOK,
    )

    first_name= models.CharField(
        max_length=30,


    )
    last_name=models.CharField(
        max_length=40,
        null=True,
        blank=True,
    )
    egn = models.CharField(
        default='',
        max_length=10,
        unique=True,
        verbose_name='EGN',
        validators=[MinLengthValidator(10)]
    )
    job_title=models.IntegerField(
        default='',
        choices=(
            (SOFTWARE_DEVELOPER,'Software Developer'),
            (QA_ENGINEER,'QA Engineer'),
            (DEVOPS_SPECIALIST,'DevOps Specialist')
        )
    )
    company = models.CharField(
        max_length=max(len(c) for c in COMPANIES),
        choices=((c,c) for c in COMPANIES)
    )
    #one to many
    deparment = models.ForeignKey(Department,on_delete=models.CASCADE)
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='profiles',
    )
    def __str__(self):
        return f"{self.first_name} employee"

    class Meta:
        ordering = ('id',)


class User(models.Model):
    email=models.EmailField()
    #one to one
    employee=models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )
class Project (models.Model):
    name = models.CharField(max_length=30)
    deadline = models.DateField(null=True,blank=True)
    #many to many
    employee_id = models.ManyToManyField(Employee)