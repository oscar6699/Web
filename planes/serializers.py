from django.db.models import fields
from rest_framework import serializers
from .models import Plan

class Planserielizers (serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'
        #fields = ["NombrePlan","descripcion","precio","fecha"]
