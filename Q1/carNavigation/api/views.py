from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime

from .serializers import NavigationRecordSerializer
from .models import NavigationRecord
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Navigation Records in Last 48 Hours':'/records/',
        }
    return Response(api_urls, status=status.HTTP_200_OK)

@api_view(['GET'])
def lastNavigationRecords(request):
    last_points=[]
    current_datetime = datetime.now() # get current datetime
    two_day=2880 #minutes == 48 hours

    records = NavigationRecord.objects.prefetch_related('vehicle') # get all records
    serializer = NavigationRecordSerializer(records, many=True)

    for record in serializer.data:
        vehicle_datetime = datetime.strptime(record["datetime"], '%d-%m-%Y %H:%M:%S') # get string format datetimes in db and change to datetime object
        result = (current_datetime-vehicle_datetime).total_seconds()/60  # get the time difference in minute type
        if (result<=two_day): 
            last_points.append(record)
            
    return Response(last_points, status=status.HTTP_200_OK)