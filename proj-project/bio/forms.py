from django.forms import ModelForm, TextInput
from .models import State

class inputForm(ModelForm):

    class Meta:
        model = State
        fields = ['name']
