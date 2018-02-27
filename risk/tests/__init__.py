import random
import factory
from django.utils import timezone
from django.contrib.auth.models import User
from ..models import (ChoicesField,
                      Fields,
                      RiskType,
                      RisksFields,
                      Risk, )

from ..enums import FIELD_TYPES


# pylint: disable=no-init, old-style-class, too-few-public-methods
class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    email = 'admin@admin.com'
    username = 'admin'
    password = factory.PostGenerationMethodCall('set_password', 'adm1n')

    is_superuser = True
    is_staff = True
    is_active = True


# pylint: disable=no-init, old-style-class, too-few-public-methods
class ChoicesFieldFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ChoicesField

    name = factory.Faker('first_name')


# pylint: disable=no-init, old-style-class, too-few-public-methods
class FieldsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Fields

    field_type = random.randint(1, 12)
    field_name = factory.Faker('first_name')
    char_field = factory.Faker('first_name')
    text_field = factory.Faker('text')
    email_field = factory.LazyAttribute(lambda fields: '{}@example.com'.format(fields.char_field))
    boolean_field = True
    date_time_field = factory.Faker('date_time', tzinfo=timezone.utc)
    file_field = factory.django.FileField(filename='the_file.dat')
    image_field = factory.django.ImageField(color='blue')
    decimal_field = random.randint(10, 12)
    float_field = random.randint(10, 12)
    choices_field = factory.SubFactory(ChoicesFieldFactory)


class RiskTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RiskType

    name = factory.Faker('first_name')


class RiskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Risk
    
    name = factory.Faker('first_name')
    risk_type = factory.SubFactory(RiskTypeFactory)


class RisksFieldsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RisksFields

    risk = factory.SubFactory(RiskFactory)
    fields = factory.SubFactory(FieldsFactory)


class RisksWithFieldsFactory(FieldsFactory):
    fields = factory.RelatedFactory(RisksFieldsFactory, 'fields')


class RisksWith2FieldsFactory(FieldsFactory):
    fields1 = factory.RelatedFactory(RisksFieldsFactory, 'fields', risk__name='Risk1')
    fields2 = factory.RelatedFactory(RisksFieldsFactory, 'fields', risk__name='Risk2')
