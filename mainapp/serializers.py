from dataclasses import fields
from pkgutil import read_code
from rest_framework import serializers
from .models import Tank

# class TankSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tank
#         fields = ['name', 'type', 'lvl', 'premium']

class TankListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tank
        fields = ['name', 'premium'] 


class TankSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        return Tank(**validated_data)

    def update(self, instanse, validated_data):
        instanse.update(**validated_data)
        return instanse.save()