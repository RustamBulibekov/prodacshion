from django import forms

from .models import VacancyCompany, ResumeEmployers


class VacancyForm(forms.ModelForm):
    class Meta:
        model = VacancyCompany
        fields = ('title', 'first_name', 'last_name', 'phone', 'vacancy', 'comment', 'email')


class ResumeForm(forms.ModelForm):
    class Meta:
        model = ResumeEmployers
        fields = ('title', 'first_name', 'last_name', 'resume', 'comment', 'phone', 'email')
