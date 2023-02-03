from django.contrib import admin
from .models import UserEmployer, UserCompany


# Register your models here.

@admin.register(UserCompany)
class UserCompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(UserEmployer)
class UserEmployerAdmin(admin.ModelAdmin):
    pass


