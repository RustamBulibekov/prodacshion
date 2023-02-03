from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import UserEmployer, UserCompany


# User = get_user_model()


class EmployerCreationForm(UserCreationForm):
    email = forms.EmailField(label=_("Email"), max_length=254, )

    class Meta(UserCreationForm.Meta):
        model = UserEmployer
        fields = ("email", "username", "name",)


class CompanyCreationForm(UserCreationForm):
    email = forms.EmailField(label=_("Email"), max_length=254, )

    class Meta(UserCreationForm.Meta):
        model = UserCompany
        fields = ("email", "username", "name", "company",)


