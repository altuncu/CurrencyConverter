from django.http import HttpResponse
from django.views.generic import FormView
from .models import Converter
from .forms import ConverterForm

class ConverterPage(FormView):
    template_name = 'converter.html'
    success_url = '/result/'
    form_class = ConverterForm

    def form_valid(self, form):
        return HttpResponse("Success.")
