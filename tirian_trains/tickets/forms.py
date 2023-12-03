from django import forms
from .models import Passenger

class LoginForm(forms.Form):
    user_id = forms.IntegerField(label='User ID')


class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['last_name', 'given_name', 'middle_initial', 'birth_date', 'gender']
        widgets = {
            'date': forms.DateInput(attrs=dict(type='date'))
        }
