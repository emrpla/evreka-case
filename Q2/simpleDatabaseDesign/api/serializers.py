from rest_framework import serializers
from .models import Bin,Operation,Bin_Operation

class BinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bin
        fields = ['id','latitute','longitude']

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ['id','name']

class BinOperationSerializer(serializers.ModelSerializer):
    bin_id = BinSerializer(read_only=True)
    operation_id = OperationSerializer(read_only=True)
    
    class Meta:
        model = Bin_Operation
        fields = ["id","bin_id","operation_id","collection_frequency"]