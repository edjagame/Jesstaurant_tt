from django import forms
from .models import Passenger

class LoginForm(forms.Form):
    customer_id = forms.IntegerField(label='User ID')


class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['last_name', 'given_name', 'middle_initial', 'birth_date', 'gender']
        widgets = {
            'birth_date': forms.DateInput(attrs=dict(type='date'))
        }
