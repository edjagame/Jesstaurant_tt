import datetime
from django.db import models
from django.urls import reverse

class Train(models.Model):
    train_id = models.IntegerField(primary_key=True, default=000000)
    series_type_choices = [
        ('S','S'),
        ('A','A')
    ]
    series_type = models.CharField(max_length=1, default='A')
    model_number = models.IntegerField(default=0)
    max_speed = models.IntegerField(default=0) 
    num_seats = models.IntegerField(default=0)
    num_toilets = models.IntegerField(default=0)
    has_reclining_seats = models.BooleanField(default=False)
    has_folding_tables = models.BooleanField(default=False)
    has_disability_access = models.BooleanField(default=False)
    has_luggage_storage = models.BooleanField(default=False)
    has_vending_machines = models.BooleanField(default=False)
    has_food_service = models.BooleanField(default=False)

    def model(self):
        return f"{self.series_type}-{str(self.model_number)}"

    def __str__(self):
        return f"{self.train_id}: {self.model()}"

    def get_absolute_url(self): 
        return reverse('trains:train-details', kwargs={'pk':self.pk})
    

class Maintenance(models.Model):
    train=models.ForeignKey(Train, on_delete=models.CASCADE)
    maintenance_id = models.IntegerField(primary_key=True, default=000000)
    date = models.DateField(default=datetime.date.today)
    crew_in_charge = models.CharField(max_length=200, default="John Doe")
    task = models.CharField(max_length=200, default="Routine inspection")
    condition_choices = [
        ('Terrible','Terrible'),
        ('Bad','Bad'),
        ('Good','Good'),
        ('Very Good','Very Good'),
        ('Excellent','Excellent')
    ]
    condition = models.CharField(max_length=10, choices=condition_choices,default="Good")

    def __str__(self):
        return f"{self.maintenance_id}: {self.date} - {self.task}"

    def get_absolute_url(self): 
        return reverse('trains:maintenance-details', kwargs={'pk':self.pk})

