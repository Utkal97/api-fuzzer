from django import forms
from .models import SwaggerFile

class SwaggerFileForm(forms.ModelForm):
    class Meta:
        model = SwaggerFile
        fields = ['file']