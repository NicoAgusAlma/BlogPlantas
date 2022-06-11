from django import forms
from problemas.models import Problema

choice_list = [('Alto', 'Alto'),('Medio', 'Medio'),('Bajo', 'Bajo')]

class ProblemaCustom(forms.ModelForm):
    class Meta:
        model=Problema
        fields = '__all__'
        widgets = {
            'peligro': forms.Select(choices=choice_list),            
        }