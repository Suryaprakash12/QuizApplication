from django.forms import ModelForm
from .models import Quiz

class Register(ModelForm):
    class Meta:
        model=Quiz
        fields='__all__'

