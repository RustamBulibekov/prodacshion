from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import EmployerCreationForm, CompanyCreationForm


class EmployerRegisterView(View):
    template_name = 'registration/register_employer.html'

    def get(self, request, *args, **kwargs):
        context = {
            'form': EmployerCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = EmployerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=password)
            login(request, user)
            gr_job = Group.objects.get(name='Employers')

            user.groups.add(gr_job)
            user.save()
            return redirect('main')
        context = {
            'form': form
        }
        return render(request, template_name='registration/register_employer.html', context=context)


class CompanyRegisterView(View):
    template_name = 'registration/register_company.html'

    def get(self, request, *args, **kwargs):
        context = {
            'form': CompanyCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = CompanyCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=password)
            login(request, user)
            gr_job = Group.objects.get(name='Companies')
            user.groups.add(gr_job)
            user.save()
            return redirect('main')
        context = {
            'form': form
        }
        return render(request, template_name='registration/register_company.html', context=context)


