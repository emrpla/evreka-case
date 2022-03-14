from rest_framework import serializers
from .models import Vehicle,NavigationRecord

class VehicleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vehicle
		fields ="__all__"

class NavigationRecordSerializer(serializers.ModelSerializer):
	datetime = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
	
	class Meta:
		model = NavigationRecord
		fields = ["latitute","longitude","vehicle_plate","datetime"]