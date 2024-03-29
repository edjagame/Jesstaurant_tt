from datetime import datetime
from django.db import models
from django.urls import reverse

class Station(models.Model):
    station_id = models.IntegerField(primary_key=True, default=000000)
    name = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.station_id}: {self.name}"

    def get_absolute_url(self): 
        return reverse('scheduled-trip:station-details', kwargs={'pk':self.pk})


class Route(models.Model):
    route_id = models.IntegerField(primary_key=True, default=000000)
    route_type_choices = [
        ('Local', 'Local'),
        ('Inter-town', 'Inter-town')
    ]
    route_type = models.CharField(max_length=10, choices=route_type_choices)
    pricing_date_start = models.DateField(auto_now_add=True)
    price = models.FloatField(default=0)
    start_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='start')
    end_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='end')

    def __str__(self):
        return f"{self.route_id}: {self.start_station} - {self.end_station}"

    def get_absolute_url(self): 
        return reverse('scheduled-trip:route-details', kwargs={'pk':self.pk})



class Trip(models.Model):
    trip_id = models.IntegerField(primary_key=True, default=000000)
    departure = models.DateTimeField(auto_now_add=True)
    arrival = models.DateTimeField(auto_now_add=True)
    route = models.ForeignKey(Route, on_delete=models.CASCADE) 
    train = models.ForeignKey("trains.Train", on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.trip_id}"

    def get_absolute_url(self):
        return reverse('scheduled-trip:trip-details', kwargs={'pk':self.pk})

