from rest_framework import serializers
from mainapp.models import Tank

class TankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tank
        fields = ['name', 'type', 'lvl', 'premium']