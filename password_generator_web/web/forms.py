from django import forms


class UniquePassForm(forms.Form):
    number_of_letters = forms.IntegerField(min_value=0,  widget=forms.NumberInput(attrs={'placeholder': 'Number of letters'}))
    number_of_numbers = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Number of numbers'}))
    number_of_symbols = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Number of symbols'}))



class EncryptionPass(forms.Form):
    your_password = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'You text to encrypt'}))
    encrypter_key = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'placeholder': 'Secret number key'}))


