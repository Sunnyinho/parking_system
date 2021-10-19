from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Owner(models.Model):
    username = models.CharField(blank=False, null=False, max_length=50, unique=True)
    password =  models.CharField(blank=False, null=False, max_length=50)
    contact = models.DecimalField(blank=False, null=False, decimal_places=0 , max_digits=10)
    company_name = models.CharField(blank=False, null=False, max_length=50)
    owner = models.ForeignKey(User, related_name="owner", on_delete=models.CASCADE, null = True )
    is_admin = models.BooleanField(default=True)
