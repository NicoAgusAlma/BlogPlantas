from django import forms
from plantas.models import Planta

class PlantaCustom(forms.ModelForm):
   
    class Meta:
        model=Planta
        
        fields = '__all__'
        widgets = {
            'nombreComun': forms.TextInput(attrs={'palceholder':'Nombre comun'}), 
            'interior': forms.CheckboxInput(attrs={'style':'margin-left:10px'}),
            'luzDirecta': forms.CheckboxInput(attrs={'style':'margin-left:10px'})                    
        }

# CON EL SIGUIENTE CODIGO SE REALIZAN LAS PRUEBAS
# SE LE VAN QUITANDO DE AQUI LOS CAMPOS A PROBAR YA QUE SUS DATOS SE INGRESARAN EN VIEWS CON UN RANDOM
# AQUI SOLO QUEDAN IMAGEN, VIVEROS, PELIGROS, INTERIOR, LUZ, DESCRIPCION PORQUE EN EL VIEWS SE PONEN
# EN PRUEBA NOMBRECOMUN, NOMBRECIENTIFICO, FAMILIA, SUSTRATO, PRECIO, FRECUENCIARIEGO.

# class PlantaCustom(forms.ModelForm):
   
#     class Meta:
#         model=Planta
        
#         fields = ['imagen','viveros','peligrosComunes','interior','luzDirecta','descripcion']
#         



