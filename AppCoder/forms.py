from django import forms

class formularioCurso(forms.Form):

    nombre = forms.CharField()
    comision = forms.IntegerField()