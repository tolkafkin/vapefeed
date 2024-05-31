from django.core.validators import MinValueValidator, MaxValueValidator
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers

from liquids.models import ManufacturerLiquid, Liquid


@extend_schema_serializer()
class ManufacturerLiquidSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand_name = serializers.CharField(max_length=200)
    created = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return ManufacturerLiquid.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.brand_name = validated_data.get('brand_name', instance.brand_name)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance


@extend_schema_serializer()
class LiquidSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.PrimaryKeyRelatedField(queryset=ManufacturerLiquid.objects.all())
    strength = serializers.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], default=1)
    cold = serializers.BooleanField(default=False)
    taste = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Liquid.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.manufacturer = validated_data.get('manufacturer', instance.manufacturer)
        instance.strength = validated_data.get('strength', instance.strength)
        instance.cold = validated_data.get('cold', instance.cold)
        instance.taste = validated_data.get('taste', instance.taste)
        instance.save()
        return instance
