from django.conf.urls import url
from .views import RiskList, RiskDetails

urlpatterns = [
    # Allow comma separated ids list such as 123,234,345,456
    url(r'^risks/$', RiskList.as_view(), name='risk-list'),
    url(r'^risks/(?P<pk>[0-9]+)/$', RiskDetails.as_view(), name='risk.detail'),
]
