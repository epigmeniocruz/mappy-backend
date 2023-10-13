from rest_framework import serializers
from .models import Fish, FishPosition

class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = '__all__'
        lookup_field = 'PIT_code'

class FishPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishPosition
        fields = '__all__'