from .models import Apartment, Tenant
from rest_framework import serializers

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Apartment
        field = '__all__'


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Tenant
        fields = '__all__'

