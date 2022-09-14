from rest_framework import serializers
from .models import Beverages
class BeverageSerializer(serializers.ModelSerializer):
    class Meta:
        model= Beverages
        fields=['id','name','desc']