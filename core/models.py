from django.db import models
# from django.contrib.auth.models import AbstractUser
import random
import string
# Create your models here.
# class User(AbstractUser):
#     gender = models.CharField(max_length=5)

class District(models.Model):
    district_code = models.CharField(max_length=4)
    district_name = models.CharField(max_length=15)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.district_name}"

class Owner(models.Model):
    facility_owner = models.CharField(max_length=255)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.facility_owner}"

class Facility(models.Model):
    facility_code = models.CharField(max_length=8, unique=True)
    facility_name = models.CharField(max_length=25, unique=True)
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING)
    owner = models.ForeignKey(Owner, on_delete=models.DO_NOTHING)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.facility_name}"

    def validate_facility_name(self):
        if Facility.objects.filter(facility_name=self.facility_name).exists():
            raise ValidationError(
                _('Facility name already exists.'),
                code='duplicate'
            )
