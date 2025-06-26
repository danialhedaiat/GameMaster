from django.contrib.auth.models import AbstractUser
from django.db import models
from django_jalali.db import models as jmodels


# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=400)
    birthdate = jmodels.jDateField(null=True, blank=True)
    postcode = models.CharField(max_length=15)
    avatar = models.ImageField(upload_to='avatars/')

    def __str__(self):
        return self.username
