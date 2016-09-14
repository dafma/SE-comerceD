from django import forms
from .models import Orden


class OrdenCreateForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['nombre', 'apellidos', 'email', 'direccion', 'codigo_postal', 'ciudad']
        widgets={
            'nombre': forms.TextInput(attrs={'class':'mdl-textfield__input'}),
            'apellidos': forms.TextInput(attrs={'class':'mdl-textfield__input'}),
            'email':forms.EmailInput(attrs={'class':'mdl-textfield__input'}),
            'direccion': forms.TextInput(attrs={'class':'mdl-textfield__input'}),
            'codigo_postal': forms.NumberInput(attrs={'class':'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
            'ciudad': forms.TextInput(attrs={'class':'mdl-textfield__input'})
        }