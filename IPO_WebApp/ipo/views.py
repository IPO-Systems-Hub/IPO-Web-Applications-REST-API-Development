from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import IPO
from .serializers import IPOSerializer
from django.shortcuts import render


class IPOViewSet(viewsets.ModelViewSet):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['status', 'price_band', 'listing_date']
    search_fields = ['company__company_name', 'price_band']  # Allow searching by company name or price_band

def home(request):
    return render(request, 'index.html')