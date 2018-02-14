import random
import factory
from django.utils import timezone
from ..models import (ChoicesField,
                      Fields,
                      FieldType,
                      Risk, )

from ..enums import FIELD_TYPES


# pylint: disable=no-init, old-style-class, too-few-public-methods
class ChoicesFieldFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ChoicesField

    name = factory.Faker('first_name')


# pylint: disable=no-init, old-style-class, too-few-public-methods
class FieldsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Fields

    char_field = factory.Faker('first_name')
    text_field = factory.Faker('text')
    email_field = factory.LazyAttribute(lambda fields: '{}@example.com'.format(fields.char_field))
    boolean_field = True
    date_time_field = factory.Faker('date_time', tzinfo=timezone.utc)
    file_field = factory.django.FileField(filename='the_file.dat')
    image_field = factory.django.ImageField(color='blue')
    decimal_field = random.randint(10, 12)
    float_field = random.randint(10, 12)
    time_field = factory.Faker('time', tzinfo=timezone.utc)
    choices_field = factory.SubFactory(ChoicesFieldFactory)

