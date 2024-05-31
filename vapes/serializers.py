from rest_framework import serializers

from profiles.models import Profile
from vapes.models import ManufacturerVape, Vape, VapeProfile


class ManufacturerVapeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand_name = serializers.CharField(max_length=200)
    created = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return ManufacturerVape.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.brand_name = validated_data.get("brand_name", instance.brand_name)
        instance.created = validated_data.get("created", instance.created)
        instance.save()
        return instance


class VapeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    manufacturer = serializers.PrimaryKeyRelatedField(queryset=ManufacturerVape.objects.all())

    def create(self, validated_data):
        return Vape.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.manufacturer = validated_data.get('manufacturer', instance.manufacturer)
        instance.save()
        return instance


class VapeProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
    vape = serializers.PrimaryKeyRelatedField(queryset=Vape.objects.all())
    body = serializers.CharField()

    def create(self, validated_data):
        return VapeProfile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance
