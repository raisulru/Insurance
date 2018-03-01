from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import (
    RiskListSerializer, 
    RiskPostSerializer, 
    ChoicesFieldSerializer, 
    RiskTypeSerializer
    )
from .models import (
    Risk, 
    ChoicesField,
    RiskType
    )


class RiskList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Risk.objects.all().order_by('-id')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RiskPostSerializer
        return RiskListSerializer


class RiskDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Risk.objects.all()
    serializer_class = RiskListSerializer


class ChoicesList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = ChoicesField.objects.all().order_by('-id')
    serializer_class = ChoicesFieldSerializer


class RiskTypeList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = RiskType.objects.all().order_by('-id')
    serializer_class = RiskTypeSerializer