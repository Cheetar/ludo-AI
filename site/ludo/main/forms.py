from django import forms

class SubmitNewSolution(forms.Form):
    title = forms.CharField(label="Nazwa rozwiązania", max_length=200)
    code = forms.CharField(label="Kod źródłowy", max_length=20000)
