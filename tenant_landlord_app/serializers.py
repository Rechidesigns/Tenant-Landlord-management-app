from .models import Apartment, Tenant
from rest_framework import serializers

class ApartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Apartment
        fields = "__all__"



class TenantSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tenant
        fields = "__all__"


