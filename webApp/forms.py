from django import forms

class CreateTag(forms.Form):
    symbol = forms.CharField(label="Símbolo del tag", initial="")

