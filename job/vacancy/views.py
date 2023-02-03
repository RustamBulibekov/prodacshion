from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, View
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import Http404
from .models import VacancyCompany, ResumeEmployers
from .forms import VacancyForm, ResumeForm


# Create your views here.
class VacancyListView(ListView):
    template_name = 'vacancy_list.html'
    model = VacancyCompany
    context_object_name = 'vacancy'


class CreateVacancyView(PermissionRequiredMixin, View):
    template_name = 'create_vacancy.html'

    def get(self, request, *args, **kwargs):
        context = {
            'form': VacancyForm()
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()
        context = {
            'form': form
        }
        return render(request, template_name='create_vacancy.html', context=context)

    def has_permission(self):
        if self.request.user.groups.filter(name='Companies').exists():
            return True


# class CreateVacancyView(PermissionRequiredMixin, CreateView):
#     groups = Group.objects.filter(name='Companies')
#     print(groups)
#
#     template_name = 'create_vacancy.html'
#     success_url = '/'
#     form_class = VacancyForm
#

# def has_permission(self):
#     if not self.request.user.groups.filter(name='Companies').exists():
#         raise Http404


class ResumeListView(ListView):
    template_name = 'resume_list.html'
    model = ResumeEmployers
    context_object_name = 'resume'


class CreateResumeView(CreateView):
    template_name = 'create_resume.html'
    success_url = '/'
    form_class = ResumeForm
