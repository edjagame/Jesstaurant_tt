from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import LoginForm, PassengerForm
from .models import Passenger, Ticket
from scheduled_trips.models import Trip

def homepage_view(request):
    return render(request, 'tickets/homepage.html')

def passenger_sign_in_view(request):
    return render(request, 'tickets/passenger-sign-in.html')

def book_ticket_interface_view(request):
    if request.method == 'POST':
        customer_id=request.POST.get("customer_id")
        trip_id=request.POST.get("trip_id")
        request.session['customer_id'] = customer_id
        request.session['trip_id'] = trip_id
        return redirect('tickets:confirm-booking')
    context = {'user':Passenger.objects.get(pk=request.session.get("customer_id")),
               'Trips':Trip.objects.all()
               }
    return render(request, 'tickets/book-ticket-interface.html', context)

def confirm_booking_view(request):
    if request.method == 'POST':
        customer_id=request.POST.get("customer_id")
        trip_id=request.POST.get("trip_id")
        customer = Passenger.objects.get(pk=customer_id)
        trip = Trip.objects.get(pk=trip_id)

        used_tickets=list(Ticket.objects.values_list('ticket_id', flat=True))
        i=1
        while(True):
            if i in used_tickets:
                i+=1
            else:
                ticket_id=i
                break

        t = Ticket(ticket_id=ticket_id, passenger=customer, trip=trip)
        t.save()
        context = {'ticket':t}
        return render(request, 'tickets/thank-you.html', context)
    context = {'user':Passenger.objects.get(pk=request.session.get("customer_id")),
               'trip':Trip.objects.get(pk=request.session.get("trip_id"))
            }
    return render(request, 'tickets/confirm-booking.html', context)

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


