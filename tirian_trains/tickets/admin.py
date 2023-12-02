from django.contrib import admin
from .models import Passenger, Ticket

class PassengerAdmin(admin.ModelAdmin):
    model = Passenger


class TicketAdmin(admin.ModelAdmin):
    model = Ticket


admin.site.register(Passenger, PassengerAdmin)
admin.site.register(Ticket, TicketAdmin)
