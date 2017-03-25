from django import forms
from exchange.models import Converter
from Currency.currencyConverter import convert

CURRENCIES = (
    ('AUD', 'Australian Dollar'),
    ('BRL', 'Brazilian Real'),
    ('GBP', 'British Pound'),
    ('CAD', 'Canadian Dollar'),
    ('CNY', 'Chinese Yuan Renminbi'),
    ('CZK', 'Czech Koruna'),
    ('DKK', 'Danish Krone'),
    ('EUR', 'Euro'),
    ('HKD', 'Hong Kong Dollar'),
    ('HUF', 'Hungarian Forint'),
    ('INR', 'Indian Rupee'),
    ('IDR', 'Indonesian Rupiah'),
    ('ILS', 'Israeli New Shekel'),
    ('JPY', 'Japanese Yen'),
    ('KRW', 'Korean Won'),
    ('MYR', 'Malaysian Ringgit'),
    ('MXN', 'Mexican Peso'),
    ('NZD', 'New Zealand Dollar'),
    ('NOK', 'Norwegian Krone'),
    ('PHP', 'Philippine Peso'),
    ('PLN', 'Polish Zloty'),
    ('RUB', 'Russian Ruble'),
    ('SGD', 'Singapore Dollar'),
    ('ZAR', 'South African Rand'),
    ('SEK', 'Swedish Krona'),
    ('CHF', 'Swiss Franc'),
    ('THB', 'Thai Baht'),
    ('TRY', 'Turkish Lira'),
    ('USD', 'US Dollar'),
)

class ConverterForm(forms.ModelForm):
    error_css_class = 'error'

    curr1 = forms.ChoiceField(choices=CURRENCIES, required=True, label='Currency1' )
    curr2 = forms.ChoiceField(choices=CURRENCIES, required=True, label='Currency2' )


    class Meta:
        model = Converter
        fields = '__all__'

        widgets = {
            'amount': forms.TextInput(attrs={'type': 'number'})
        }

    def result(self):
        return self.data['amount'] + " " + self.data['curr1'] + " is " + convert(self.cleaned_data['curr1'], self.cleaned_data['curr2'], self.cleaned_data['amount']) + " " + self.data['curr2']
