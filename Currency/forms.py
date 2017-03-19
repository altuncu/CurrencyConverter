from django import forms

class CurrForm(forms.Form):
    first = forms.CharField(label='first', max_length=100)
    second = forms.CharField(label='second', max_length=100)
