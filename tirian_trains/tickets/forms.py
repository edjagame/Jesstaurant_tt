import datetime

from django import forms
from .models import Passenger
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    customer_id = forms.IntegerField(label='User ID')
    
    def clean_customer_id(self):
        customer_id = self.cleaned_data["customer_id"]
        if customer_id not in list(Passenger.objects.values_list('customer_id', flat=True)):
            raise ValidationError(
                "User does not exist."
            )
        return customer_id


class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['last_name', 'given_name', 'middle_initial', 'birth_date', 'gender']
        widgets = {
            'birth_date': forms.DateInput(attrs=dict(type='date'))
        }


    def clean_birth_date(self):
        birth_date = self.cleaned_data["birth_date"]
        if birth_date:
            if birth_date > datetime.date.today():
                raise ValidationError(
                    "Not yet born."
                )
        return birth_date
