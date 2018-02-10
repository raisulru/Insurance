from rest_framework.serializers import ModelSerializer
from .models import Risk, FieldType, Fields, ChoicesField


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


class FieldTypeSerializer(ModelSerializer):
    field_value = FieldsSerializer()

    class Meta:
        model = FieldType
        fields = (
            'field_type',
            'field_name',
            'field_value'
        )


class RiskListSerializer(ModelSerializer):
    fields = FieldTypeSerializer(many=True)

    class Meta:
        model = Risk
        fields = (
            'id',
            'name',
            'fields'
        )


class RiskPostSerializer(ModelSerializer):
    fields = FieldTypeSerializer()

    class Meta:
        model = Risk
        fields = (
            'id',
            'name',
            'fields'
        )
