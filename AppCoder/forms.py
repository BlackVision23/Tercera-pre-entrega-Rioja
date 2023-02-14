from django import forms

class formularioCurso(forms.Form):

    nombre = forms.CharField()
    comision = forms.IntegerField()

class formularioProfes(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()

class formularioEntregables(forms.Form):

    nombre = forms.CharField()
    fechaDeEntrega = forms.DateField()
    entregado = forms.BooleanField()