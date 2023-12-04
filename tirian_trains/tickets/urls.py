from django.urls import path
from .views import (
            homepage_view, passenger_login_view, passenger_create_view, passenger_sign_in_view,
            book_ticket_interface_view, confirm_booking_view, confirm_remove_view
        )

urlpatterns = [
        path("", homepage_view, name="homepage"),
        path("login", passenger_login_view, name="passenger-login"),    
        path("create-user", passenger_create_view, name="passenger-create"),
        path("sign-in", passenger_sign_in_view, name="passenger-sign-in"),
        path("book-ticket", book_ticket_interface_view, name="book-ticket"),
        path("confirm-booking", confirm_booking_view, name="confirm-booking"),
        path("confirm-remove", confirm_remove_view, name="confirm-remove")
]

app_name = "tickets"
