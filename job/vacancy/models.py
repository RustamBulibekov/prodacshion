from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class ResumeEmployers(models.Model):
    title = models.CharField(max_length=20, verbose_name='title of your resume')
    first_name = models.CharField(max_length=20, verbose_name='Your first name')
    last_name = models.CharField(max_length=20, verbose_name='Your last name')
    resume = models.TextField(verbose_name='Your resume')
    comment = models.TextField(verbose_name='Information', blank=True)
    phone = PhoneNumberField(unique=True, blank=False, null=False, verbose_name='Your number phone')
    email = models.EmailField(unique=True, null=False, blank=False, verbose_name='Your email')

    def __str__(self):
        return self.title


class VacancyCompany(models.Model):
    title = models.CharField(max_length=20, verbose_name='title of your vacancy')

    first_name = models.CharField(max_length=20, verbose_name='Your first name')
    last_name = models.CharField(max_length=20, verbose_name='Your last name')
    vacancy = models.TextField(verbose_name='Your vacancy')
    comment = models.TextField(verbose_name='Information', blank=True)
    phone = PhoneNumberField(unique=True, blank=False, null=False, verbose_name='Your number phone')
    email = models.EmailField(unique=True, null=False, blank=False, verbose_name='Your email')

    def __str__(self):
        return self.title
