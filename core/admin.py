from django.contrib import admin
from .models import Facility, District, Owner
# from django.contrib.auth.admin import UserAdmin
# Register your models here.
# class CustomUserAdmin(UserAdmin):
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('gender',)}),
#         # Add more fieldsets if necessary
#     )
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {'fields': ('gender',)}),
#         # Add more add_fieldsets if necessary
#     )

# admin.site.register(User, CustomUserAdmin)
admin.site.register(Facility)
admin.site.register(District)
admin.site.register(Owner)