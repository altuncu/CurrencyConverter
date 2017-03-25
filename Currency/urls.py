from django.conf.urls import include, url
from exchange.views import ConverterPage

urlpatterns = [
    url(r'^', ConverterPage.as_view())
]
