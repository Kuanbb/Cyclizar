from django import forms
from .models import Usuario

class Form_Register_User(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'