from django.shortcuts import render
from rest_framework import generics
from .serializers import RiskListSerializer, RiskPostSerializer
from .models import Risk


# Create your views here.
class RiskList(generics.ListCreateAPIView):
    queryset = Risk.objects.all()
    serializer_class = RiskListSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RiskPostSerializer
        return RiskListSerializer


class RiskDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Risk.objects.all()
    serializer_class = RiskListSerializer
