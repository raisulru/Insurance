from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Risk, RiskType, Fields, ChoicesField, RisksFields
from django.db import transaction



class ChoicesFieldSerializer(ModelSerializer):

    class Meta:
        model = ChoicesField
        fields = (
            'name',
        )


class FieldsSerializer(ModelSerializer):
    choices_field = ChoicesFieldSerializer()

    class Meta:
        model = Fields
        fields = (
            'field_name',
            'field_type',
            'char_field',
            'text_field',
            'email_field',
            'boolean_field',
            'date_time_field',
            'file_field',
            'image_field',
            'decimal_field',
            'float_field',
            'time_field',
            'url_field',
            'choices_field',
        )


class RiskTypeSerializer(ModelSerializer):

    class Meta:
        model = RiskType
        fields = (
            'name',
        )


class RiskListSerializer(ModelSerializer):
    fields = FieldsSerializer(many=True, read_only=True)
    risk_type = RiskTypeSerializer()

    class Meta:
        model = Risk
        fields = (
            'id',
            'name',
            'risk_type',
            'fields'
        )


class RiskPostSerializer(ModelSerializer):
    fields = FieldsSerializer(many=True)
    risk_type = RiskTypeSerializer()

    class Meta:
        model = Risk
        fields = (
            'id',
            'name',
            'risk_type',
            'fields'
        )

    def create(self, validated_data):
        print('its magic')
        field_items = validated_data.pop('field_items', []),

        risk = Risk.objects.create(**validated_data)

        return risk

