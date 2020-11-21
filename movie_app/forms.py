from django import forms

class MovieForm(forms.Form):
    title = forms.CharField(label="Tytuł")
    year = forms.IntegerField(label="Rok")