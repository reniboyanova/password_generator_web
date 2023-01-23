from django import forms


class UniquePassForm(forms.Form):
    number_of_letters = forms.IntegerField(min_value=0)
    number_of_numbers = forms.IntegerField(min_value=0)
    number_of_symbols = forms.IntegerField(min_value=0)

