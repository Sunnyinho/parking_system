from django.db import models
from owner.models import  Owner
# Create your models here.
class ParkingInput(models.Model):
    admin = models.ForeignKey(Owner, default=None, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    parking_space = models.DecimalField(max_digits=10, decimal_places=0)


class ParkingTable(models.Model):
    admin = models.ForeignKey(Owner, default=None, on_delete=models.CASCADE)
    vehicle_no = models.CharField(blank=False, null=False, max_length=20)
    reserved = models.DecimalField(max_digits=3, decimal_places=0 )
    less_than_1hr = models.BooleanField(default=False)
    more_than_1hr = models.BooleanField(default=False)
    is_occupied = models.BooleanField(default=False)