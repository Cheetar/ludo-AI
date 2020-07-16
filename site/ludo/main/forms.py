from django import forms

class SubmitNewSolution(forms.Form):
    title = forms.CharField(label="Title", max_length=200)
    code = forms.CharField(label="Source Code", max_length=20000)
