from django.conf.urls import url
from .views import RiskList

urlpatterns = [
    # Allow comma separated ids list such as 123,234,345,456
    url(r'^$', RiskList.as_view(), name='risk-list'),
]
