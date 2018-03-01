from django.contrib import admin
from .models import Risk, RiskType, Fields, ChoicesField, RisksFields


class RiskAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'risk_type',
    ]
# Register your models here.
admin.site.register(Risk, RiskAdmin)
admin.site.register(RiskType)
admin.site.register(Fields)
admin.site.register(ChoicesField)
admin.site.register(RisksFields)