from django import forms
from .models import Plan_Contratado
from django.contrib.auth.models import User

class PlanForm(forms.ModelForm):

    class Meta:
        model = Plan_Contratado
        fields = {'idPlan'}