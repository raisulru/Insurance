from django.shortcuts import render
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly
from .serializers import RiskListSerializer, RiskPostSerializer
from .models import Risk


# Create your views here.
class RiskList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )
    queryset = Risk.objects.all().order_by('-id')
    serializer_class = RiskListSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RiskPostSerializer
        return RiskListSerializer


class RiskDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Risk.objects.all()
    serializer_class = RiskListSerializer
