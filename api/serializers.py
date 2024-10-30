from rest_framework import serializers
from .models import devPlanning

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = devPlanning
        fields = '__all__'
