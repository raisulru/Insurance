from django.shortcuts import render
from rest_framework import generics
from .serializers import RiskSerializer
from .models import Risk


# Create your views here.
class RiskList(generics.ListCreateAPIView):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer