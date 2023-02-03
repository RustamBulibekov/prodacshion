from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_('email address'),
                              unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class UserEmployer(User):
    name = models.CharField(max_length=20, verbose_name='Employer name')


class UserCompany(User):
    company = models.CharField(max_length=30, verbose_name='Company name', blank=True)
    name = models.CharField(max_length=20, verbose_name='Use name if you are not company', blank=True)


