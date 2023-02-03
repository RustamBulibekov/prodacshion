from django.contrib import admin
from .models import VacancyCompany, ResumeEmployers
# Register your models here.


@admin.register(VacancyCompany)
class VacancyAdmin(admin.ModelAdmin):
    pass


@admin.register(ResumeEmployers)
class ResumeAdmin(admin.ModelAdmin):
    pass


