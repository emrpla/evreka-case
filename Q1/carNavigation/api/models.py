from django.db import models
import uuid

# Create your models here.

class Vehicle(models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    plate = models.CharField(max_length=20)
    def __str__(self):
        return self.plate


class NavigationRecord(models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    vehicle =  models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    latitute = models.FloatField(default=0) 
    longitude = models.FloatField(default=0) 
    
    @property
    def vehicle_plate(self):
        plate = self.vehicle.plate  
        return plate