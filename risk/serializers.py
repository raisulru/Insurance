import logging
from django.db import transaction
from django.db.utils import IntegrityError
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Risk, RiskType, Fields, ChoicesField, RisksFields
from django.db import transaction

logger = logging.getLogger(__name__)


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
    field_items = serializers.JSONField(write_only=True, required=False, allow_null=True)

    class Meta:
        model = Risk
        fields = (
            'id',
            'name',
            'risk_type',
            'field_items'
        )

    def create_fields(self, risk, fields):
        if fields:
            for field in fields:
                # try:
                item = Fields.objects.create(
                    field_name=field['field_name'],
                    field_type=field['field_type'],
                    char_field=field['char_field'],
                    text_field=field['text_field'],
                    email_field=field['email_field'],
                    boolean_field=field['boolean_field'],
                    date_time_field=field['date_time_field'],
                    file_field=field['file_field'],
                    image_field=field['image_field'],
                    decimal_field=field['decimal_field'],
                    float_field=field['float_field'],
                    time_field=field['time_field'],
                    url_field=field['url_field'],
                    choices_field=field['choices_field'],
                    )
                RisksFields.objects.create(risk=risk, fields=item)
                # except IntegrityError as exception:
                #     # exception caught
                #     logger.info("{} Exception Caught".format(exception))
                #     continue

    def create(self, validated_data):
        fields = validated_data.pop('field_items', [])
        risk = Risk.objects.create(**validated_data)

        self.create_fields(risk, fields)

        return risk

