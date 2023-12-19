from rest_framework import serializers
from .models import Location
class LocationSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=25)
    class Meta:
        model = Location
        fields = ['id', 'name','service_name','parent_location']