from rest_framework.serializers import ModelSerializer
from .models import Risk


class RiskSerializer(ModelSerializer):

    class Meta:
        model = Risk
        fields = (
            'name',
            'fields'
        )
