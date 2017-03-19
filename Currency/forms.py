from django import forms
from .models import Converter

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

    curr1 = forms.ChoiceField(choices=CURRENCIES, required=True )
    curr2 = forms.ChoiceField(choices=CURRENCIES, required=True )

    class Meta:
        model = Converter

        widgets = {
            'amount': forms.TextInput(attrs={'placeholder': '1.0'})
        }
