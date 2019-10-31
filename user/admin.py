from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models


# Register your models here.
#class UserAdmin(admin.ModelAdmin):
 #   list_display = ('id', 'name', 'phone')

admin.site.register(models.User, UserAdmin)


#class AddressAdmin(admin.ModelAdmin):
#    list_display = ('user', 'receiver', 'addr', 'zip_code', 'phone')

admin.site.register(models.Address)
