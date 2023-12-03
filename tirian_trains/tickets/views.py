from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import LoginForm, PassengerForm
from .models import Passenger
from scheduled_trips.models import Trip

def homepage_view(request):
    return render(request, 'tickets/homepage.html')

def passenger_sign_in_view(request):
    return render(request, 'tickets/passenger-sign-in.html')

def book_ticket_interface_view(request):
    context = {'user':Passenger.objects.get(pk=request.session.get("customer_id")),
               'Trips':Trip.objects.all()
               }
    return render(request, 'tickets/book-ticket-interface.html', context)

def passenger_login_view(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            customer_id=form.cleaned_data["customer_id"]
            request.session['customer_id'] = customer_id
            return redirect('tickets:book-ticket') 
        else:
            return render(request, 'tickets/passenger-login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'tickets/passenger-login.html', {'form': form})
    

def passenger_create_view(request):
    if request.method == 'POST':
        form = PassengerForm(request.POST)
        if form.is_valid():
            last_name = form.cleaned_data["last_name"]
            given_name = form.cleaned_data["given_name"]
            middle_initial = form.cleaned_data["middle_initial"]
            birth_date = form.cleaned_data["birth_date"]
            gender = form.cleaned_data["gender"]

            used_ids=list(Passenger.objects.values_list('customer_id', flat=True))
            i=1
            while(True):
                if i in used_ids:
                    i+=1
                else:
                    customer_id=i
                    break

            p = Passenger(
                    customer_id=customer_id, 
                    last_name=last_name, 
                    given_name=given_name,
                    middle_initial=middle_initial,
                    birth_date=birth_date,
                    gender=gender
                )
            p.save()
            
            request.session["customer_id"]=customer_id
            return redirect('tickets:book-ticket')
        else:
            return render(request, 'tickets/passenger-create.html',{'form': form})
    else:    
        form = PassengerForm()

    return render(request, 'tickets/passenger-create.html',{'form': form})


