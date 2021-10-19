from django.db import models

from owner.models import Owner
# Create your models here.

class Worker(models.Model):
    admin        = models.ForeignKey(Owner, default=None, on_delete=models.CASCADE)
    username = models.CharField(blank=False, max_length=50)
    password  = models.CharField(blank=False, max_length=50)
    is_Admin  = models.BooleanField(default=False)

