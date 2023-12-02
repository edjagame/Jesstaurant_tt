from django.contrib import admin
from .models import Station, Route, Trip

class StationAdmin(admin.ModelAdmin):
    model = Station


class RouteAdmin(admin.ModelAdmin):
    model = Route


class TripAdmin(admin.ModelAdmin):
    model = Trip


admin.site.register(Station, StationAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Trip, TripAdmin)
