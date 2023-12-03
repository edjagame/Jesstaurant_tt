from django.urls import path
from .views import (
            homepage_view, passenger_login_view, passenger_create_view, passenger_sign_in_view
        )

urlpatterns = [
        path("", homepage_view, name="homepage"),
        path("login", passenger_login_view, name="passenger-login"),    
        path("create-user", passenger_create_view, name="passenger-create"),
        path("passenger-sign-in", passenger_sign_in_view, name="passenger-sign-in")
]

app_name = "tickets"
