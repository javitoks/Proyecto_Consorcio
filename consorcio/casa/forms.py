from dataclasses import field
from django import forms

from casa.models import Propietario, Inquilino, Casa, Pago



class FormularioPropietario(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = '__all__'

    
class FormularioInquilino(forms.ModelForm):
    class Meta:
        model = Inquilino
        fields = '__all__'

class FormularioCasa(forms.ModelForm):
    class Meta:
        model = Casa
        fields = '__all__'


class FormularioPago(forms.ModelForm):
    class Meta:
        model = Pago
        fields = '__all__'