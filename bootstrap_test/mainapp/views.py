from django.shortcuts import render

from django import forms


class ExampleForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=20)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='password ', max_length=30)


# Create your views here.

def index(request):
    return render(request, 'home.html', {'form': ExampleForm})
