from datetime import datetime
from django.db import models
from django.urls import reverse

class Passenger(models.Model):
    customer_id = models.IntegerField(primary_key=True, default=0000)
    last_name = models.CharField(max_length=100, default="Doe")
    given_name = models.CharField(max_length=100, default="John")
    middle_initial = models.CharField(max_length=2, blank=True)
    birth_date = models.DateField(auto_now_add=True)
    gender = models.CharField(max_length=100, blank=True)

    def get_age(self):
        return int((datetime.date.today().year - self.birth_date.date().year) / 365.25)

    def __str__(self):
       return f"{self.customer_id} - {self.last_name}, {self.given_name} {self.middle_initial}" 

    def get_absolute_url(self):
        return reverse('tickets:passenger-details', kwargs={'pk':self.pk})


class Ticket(models.Model):
    ticket_id = models.IntegerField(primary_key=True, default=00000)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    trip = models.ForeignKey("scheduled_trips.Trip", on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"Ticket {self.ticket_id}: {self.trip.route.start_station} - {self.trip.route.end_station}" 

    def get_absolute_url(self):
        return reverse('tickets:passenger-details', kwargs={'pk':self.pk})
