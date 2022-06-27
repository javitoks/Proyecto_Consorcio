from django import forms

from casa.models import Propietario
from casa.models import Inquilino


class FormularioPropietario(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = '__all__'

    
class FormularioInquilino(forms.ModelForm):
    class Meta:
        model = Inquilino
        fields = '__all__'

