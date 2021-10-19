from django.contrib import admin
from parking.models import ParkingInput, ParkingTable
# Register your models here.
admin.site.register(ParkingInput)
admin.site.register(ParkingTable)