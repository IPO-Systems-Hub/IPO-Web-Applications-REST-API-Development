from rest_framework import serializers
from .models import IPO, Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class IPOSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = IPO
        fields = '__all__'
