from django import forms


class CreateTag(forms.Form):
    symbol = forms.CharField(label="Symbols of the tag", initial="")
