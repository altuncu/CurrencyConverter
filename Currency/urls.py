from django.conf.urls import patterns, include, url
from ads.views import ConverterPage

urlpatterns = patterns('',
    url(r'^result/', ConverterPage.as_view()),
)
