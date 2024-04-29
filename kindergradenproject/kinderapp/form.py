from django import forms
from kinderapp.models import Postupload

class EditForm(forms.ModelForm):
    class Meta:
        model = Postupload
        fields = '__all__'