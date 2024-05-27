from django import forms
#from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Facility

#User = get_user_model

class FacilityCreateForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['facility_name', 'district', 'owner']

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ("first_name","last_name","email","username")
#         field_classes = {"username": UsernameField}