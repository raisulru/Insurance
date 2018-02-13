from rest_framework.serializers import ModelSerializer
from .models import Risk, FieldType, Fields, ChoicesField
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
    fields = FieldTypeSerializer(many=True)

    class Meta:
        model = Risk
        fields = (
            'id',
            'name',
            'fields'
        )

    # @transaction.atomic
    def create(self, validated_data):
        fields_type = validated_data.pop('fields', [])
        fields = fields_type.pop('field_value', [])
        choices = fields.pop('choices_field', [])

        choice = ChoicesField(
            name=choices['name']
        )
        choice.save()

        field = Fields(
            char_field=fields['char_field'],
            text_field=fields['text_field'],
            email_field=fields['email_field'],
            boolean_field=fields['boolean_field'],
            date_time_field=fields['date_time_field'],
            # file_field=fields['file_field'],
            # image_field=fields['image_field'],
            decimal_field=fields['decimal_field'],
            float_field=fields['float_field'],
            time_field=fields['time_field'],
            url_field=fields['url_field'],
            choices_field=choice
        )
        field.save()

        manyfield = FieldType(
            field_type=fields_type['field_type'],
            field_name=fields_type['field_name'],
            field_value=field
        )
        manyfield.save()

        risk = Risk(
            **validated_data
        )

        risk.save()
        risk.fields.add(manyfield)
        return risk
