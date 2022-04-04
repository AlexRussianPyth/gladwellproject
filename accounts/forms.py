from .models import Achiever
from django import forms

class AchieverForm(forms.ModelForm):
    class Meta:
        model = Achiever
        fields = ('email', 'user_name', 'first_name', 'last_name', 'about')