from django.contrib import admin
from .models import Train, Maintenance

class TrainAdmin(admin.ModelAdmin):
    model = Train


class MaintenanceAdmin(admin.ModelAdmin):
    model = Maintenance


admin.site.register(Train, TrainAdmin)
admin.site.register(Maintenance, MaintenanceAdmin)
