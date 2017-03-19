from __future__ import unicode_literals

from django.db import models

# Create your models here.

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

class Converter(models.Model):
    amount   = models.CharField(max_length=50)
    curr1    = models.CharField(max_length=3, choices=CURRENCIES)
    curr2    = models.CharField(max_length=3, choices=CURRENCIES)
