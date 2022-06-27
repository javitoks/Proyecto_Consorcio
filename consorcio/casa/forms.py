from django import forms

from casa.models import Propietario


class FormularioPropietario(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = '__all__'

    
