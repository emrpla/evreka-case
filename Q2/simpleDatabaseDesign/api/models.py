from django.db import models
import uuid

# Create your models here.

class Bin(models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    latitude = models.FloatField(default=0) 
    longitude = models.FloatField(default=0) 


class Operation(models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Bin_Operation(models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    bin_id =  models.ForeignKey(Bin,on_delete=models.DO_NOTHING)
    operation_id =  models.ForeignKey(Operation,on_delete=models.DO_NOTHING)
    collection_frequency = models.IntegerField(default=0)
    last_collection = models.DateTimeField()