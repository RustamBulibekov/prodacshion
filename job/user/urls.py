from django.urls import path
from django.contrib.auth import views
from .views import EmployerRegisterView, CompanyRegisterView

app_name = 'user'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register_employer/', EmployerRegisterView.as_view(), name='register_employer'),
    path('register_company/', CompanyRegisterView.as_view(), name='register_company'),


]
