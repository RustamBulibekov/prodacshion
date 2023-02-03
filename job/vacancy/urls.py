from django.urls import path
from .views import VacancyListView, CreateVacancyView, CreateResumeView,ResumeListView

app_name = 'vacancy'

urlpatterns = [
    path('vacancy_list/', VacancyListView.as_view(), name='vacancy_list'),
    path('create_vacancy/', CreateVacancyView.as_view(), name='create_vacancy'),
    path('create_resume/', CreateResumeView.as_view(), name='create_resume'),
    path('resume_list/', ResumeListView.as_view(), name='resume_list'),
]
