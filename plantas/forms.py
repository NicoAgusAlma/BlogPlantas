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



# class CallForm (forms.ModelForm):

# class Meta():
#     model = Call
#     widgets = {
#          'employee_id' : forms.ChoiceField(choices=FormsTools.EmployeesToTuples(Employee.objects.all()))
#     }
# class CallForm (forms.ModelForm):
#     employee_id = forms.ChoiceField(choices=FormsTools.EmployeesToTuples(Employee.objects.all()))

#     class Meta:
#         model = Call
#         fields = ['employee_id']