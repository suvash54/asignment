from django import forms
from lfapp.models import user_data

class user_form(forms.ModelForm):
    class Meta:
        model = user_data
        fields = ['user_name','user_password']