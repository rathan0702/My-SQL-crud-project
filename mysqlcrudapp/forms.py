from django import forms
from mysqlcrudapp.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'mail': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
        }

