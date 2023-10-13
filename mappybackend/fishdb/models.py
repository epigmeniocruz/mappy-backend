from django.db import models

# Create your models here.
class Fish(models.Model):
    date_time = models.DateTimeField(blank=True, null=True)
    AT_code = models.CharField(max_length=12, primary_key=True, unique=True)
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

class FishPosition(models.Model):
    fish =models.ForeignKey(Fish, to_field="AT_code", on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    X = models.DecimalField(max_digits= 22, decimal_places=14)
    Y = models.DecimalField(max_digits= 22, decimal_places=14)
    Z = models.DecimalField(max_digits= 22, decimal_places=14, default=0.0)
    MSE = models.DecimalField(max_digits= 12, decimal_places=2, default=0.0)