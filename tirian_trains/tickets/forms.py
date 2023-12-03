import datetime

from django import forms
from .models import Passenger
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    customer_id = forms.IntegerField(label='User ID')


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
