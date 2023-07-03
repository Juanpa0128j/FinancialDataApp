from django import forms

class CreateTag(forms.Form):
    nombre = forms.CharField(label="Nombre del tag", initial="")

