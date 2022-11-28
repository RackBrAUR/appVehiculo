from itertools import pairwise
from django import forms
""" from django.contrib.auth.models import User """

from .models import Car,User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password','identificacion','telefono','pais','departamento','ciudad','direccion']



class CompareForm(forms.Form):

    car1 = forms.ModelChoiceField(
        Car.objects.all(),
        required=True,
        label='Vehículo 1',
        widget=forms.Select(
            attrs={'class': 'selectpicker', 'data-live-search': "true"}
        )
    )
    car2 = forms.ModelChoiceField(
        Car.objects.all(),
        required=True,
        label='Vehículo 2',
        widget=forms.Select(
            attrs={'class': 'selectpicker', 'data-live-search': "true"}
        )
    )

class Orden(forms.Form):
    def __init__(self,nombre,pais,departamento,ciudad,direccion,identificacion,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['nombre']=forms.CharField(
            widget=forms.TextInput(attrs={'class': 'form-control','value':nombre}))
        self.fields['pais']=forms.CharField(
            widget=forms.TextInput(attrs={'class': 'form-control','value':pais}))
        self.fields['departamento']=forms.CharField(
            widget=forms.TextInput(attrs={'class': 'form-control','value':departamento}))
        self.fields['ciudad']=forms.CharField(
            widget=forms.TextInput(attrs={'class': 'form-control','value':ciudad}))
        self.fields['address']=forms.CharField(label='direccion',
            widget=forms.TextInput(attrs={'class': 'form-control','for':'address','id':'address','value':direccion}))
        self.fields['identificacion']=forms.CharField(
            widget=forms.TextInput(attrs={'class': 'form-control','value':identificacion}))
    nombre = forms.CharField()
    pais = forms.CharField()
    departamento = forms.CharField()
    ciudad = forms.CharField()
    address = forms.CharField()
    identificacion = forms.CharField()

