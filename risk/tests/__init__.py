import random
import factory
from django.utils import timezone
from django.contrib.auth.models import User
from ..models import (ChoicesField,
                      Fields,
                      FieldType,
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


class FieldTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FieldType

    field_type = random.randint(1, 12)
    field_name = factory.Faker('first_name')
    field_value = factory.SubFactory(FieldsFactory)


class RiskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Risk

    name = factory.Faker('first_name')

    @factory.post_generation
    def fields(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of fields were passed in, use them
            for field in extracted:
                self.fields.add(field)

