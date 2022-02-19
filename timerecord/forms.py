from django import forms
from .models import Goal

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = "__all__"
        exclude = ["slug", "created_at", "is_achieved"]
