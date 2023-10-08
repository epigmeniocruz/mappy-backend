from django.db import models

# Create your models here.
class Fish(models.Model):
    date_time = models.DateTimeField(blank=True, null=True)
    AT_code = models.CharField(max_length=12)
    X = models.DecimalField(max_digits= 22, decimal_places=14)
    Y = models.DecimalField(max_digits= 22, decimal_places=14)
    Z = models.DecimalField(max_digits= 22, decimal_places=14)
    MSE = models.DecimalField(max_digits= 12, decimal_places=2)
    PIT_code = models.CharField(max_length=16)
    release_date = models.DateField(blank=True, null=True)
    species = models.CharField(max_length=12)
    detection_time = models.DateTimeField(blank = True, null=True)
    antenna_group_name = models.CharField(max_length = 50, blank = True, null=True)
    collection_status = models.BooleanField()