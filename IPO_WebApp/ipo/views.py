from rest_framework import viewsets
from .models import IPO
from .serializers import IPOSerializer
from django.shortcuts import render

class IPOViewSet(viewsets.ModelViewSet):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer

def home(request):
    return render(request, 'index.html')