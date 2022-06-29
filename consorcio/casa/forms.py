from django import forms

from casa.models import Propietario, Inquilino, Casa



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


