from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm, PassengerForm

def homepage_view(request):
    return render(request, 'tickets/homepage.html')

def passenger_sign_in_view(request):
    return render(request, 'tickets/passenger-sign-in.html')

def passenger_login_view(request):
    form = LoginForm()
    return render(request, 'tickets/passenger-login.html', {'form': form})

def passenger_create_view(request):
    form = PassengerForm
    return render(request, 'tickets/passenger-create.html',{'form': form})
