from django import forms
from app1.models import *

class SchoolForm(forms.ModelForm):
    class Meta:
        model=School
        fields='__all__'
        
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
            
