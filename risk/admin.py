from django.contrib import admin
from .models import Risk, FieldType, Fields, ChoicesField


class RiskAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = [
        'name',
        'fields'
    ]
# Register your models here.
admin.site.register(Risk, RiskAdmin)
admin.site.register(FieldType)
admin.site.register(Fields)
admin.site.register(ChoicesField)