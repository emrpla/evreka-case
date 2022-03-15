from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import BinOperationSerializer
from .models import Bin_Operation
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'All bin_operation pairs':'/bin-operation/',
        }
    return Response(api_urls, status=status.HTTP_200_OK)


@api_view(['GET'])
def binOperationPairs(request):
    records = Bin_Operation.objects.prefetch_related() # get all pairs
    serializer = BinOperationSerializer(records, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)