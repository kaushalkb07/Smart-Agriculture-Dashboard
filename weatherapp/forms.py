from django import forms

class CityForm(forms.Form):
    city = forms.CharField(
        max_length=100,
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter city name',
            'class': 'form-control',
        })
    )
