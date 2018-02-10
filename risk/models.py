from django.db import models
from .enums import FIELD_TYPES


# # Create your models here.
class ChoicesField(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Fields(models.Model):
    char_field = models.CharField(max_length=100, blank=True, null=True)
    text_field = models.TextField(blank=True, null=True)
    email_field = models.EmailField(max_length=250, blank=True, null=True)
    boolean_field = models.BooleanField(blank=True)
    date_time_field = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    file_field = models.FileField(upload_to=None, max_length=100, blank=True)
    image_field = models.ImageField(upload_to=None, max_length=100, blank=True)
    decimal_field = models.DecimalField(max_digits=25, decimal_places=10, blank=True, null=True)
    float_field = models.FloatField(blank=True, null=True)
    time_field = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    url_field = models.URLField(max_length=200, blank=True)
    choices_field = models.ForeignKey(ChoicesField, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ('char_field',)


class FieldType(models.Model):
    field_type = models.IntegerField(choices=FIELD_TYPES, default=1)
    field_name = models.CharField(max_length=100)
    field_value = models.ForeignKey(Fields, on_delete=models.CASCADE)

    def __str__(self):
        return self.field_name

    class Meta:
        ordering = ('field_name',)


class Risk(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    fields = models.ManyToManyField(FieldType)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
